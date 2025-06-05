// API functions for Django backend integration
import type { Topic, UserProgress, Vocabulary } from "@/types"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api"

// Helper function to get auth token
const getAuthToken = () => {
  if (typeof window !== "undefined") {
    return localStorage.getItem("auth-token")
  }
  return null
}

// Helper function to make authenticated requests
const makeRequest = async (url: string, options: RequestInit = {}) => {
  const token = getAuthToken()
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  }

  // Add existing headers
  if (options.headers) {
    if (options.headers instanceof Headers) {
      options.headers.forEach((value, key) => {
        headers[key] = value
      })
    } else if (Array.isArray(options.headers)) {
      options.headers.forEach(([key, value]) => {
        headers[key] = value
      })
    } else {
      Object.assign(headers, options.headers)
    }
  }

  if (token) {
    headers["Authorization"] = `Bearer ${token}`
  }

  const response = await fetch(`${API_BASE_URL}${url}`, {
    ...options,
    headers,
  })

  if (!response.ok) {
    let errorMessage = `HTTP error! status: ${response.status}`
    
    try {
      const errorData = await response.json()
      
      // Handle Django REST framework validation errors
      if (errorData.detail) {
        errorMessage = errorData.detail
      } else if (errorData.error) {
        errorMessage = errorData.error
      } else if (errorData.non_field_errors) {
        errorMessage = Array.isArray(errorData.non_field_errors) 
          ? errorData.non_field_errors.join(', ')
          : errorData.non_field_errors
      } else if (typeof errorData === 'object') {
        // Handle field-specific errors
        const fieldErrors = []
        for (const [field, errors] of Object.entries(errorData)) {
          if (Array.isArray(errors)) {
            fieldErrors.push(`${field}: ${errors.join(', ')}`)
          } else if (typeof errors === 'string') {
            fieldErrors.push(`${field}: ${errors}`)
          }
        }
        if (fieldErrors.length > 0) {
          errorMessage = fieldErrors.join('; ')
        }
      }
    } catch (parseError) {
      // If we can't parse the error response, use the status code
      if (response.status === 400) {
        errorMessage = "Dữ liệu không hợp lệ. Vui lòng kiểm tra lại thông tin."
      } else if (response.status === 409) {
        errorMessage = "Dữ liệu đã tồn tại. Vui lòng sử dụng tên khác."
      } else if (response.status === 500) {
        errorMessage = "Lỗi server. Có thể dữ liệu đã tồn tại hoặc không hợp lệ."
      }
    }
    
    throw new Error(errorMessage)
  }

  // Handle empty responses (like DELETE operations that return 204 No Content)
  const contentLength = response.headers.get('content-length')
  if (contentLength === '0' || response.status === 204) {
    return {}
  }

  // Check if response has content to parse
  const text = await response.text()
  if (!text) {
    return {}
  }

  try {
    return JSON.parse(text)
  } catch (error) {
    // If JSON parsing fails, return empty object
    console.warn('Failed to parse JSON response:', text)
    return {}
  }
}

// Auth API
export const authAPI = {
  login: async (email: string, password: string) => {
    const response = await fetch(`${API_BASE_URL}/auth/login/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.error || errorData.detail || "Login failed")
    }

    return response.json()
  },

  register: async (name: string, email: string, password: string) => {
    const response = await fetch(`${API_BASE_URL}/auth/register/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, email, password }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.error || errorData.detail || "Registration failed")
    }

    return response.json()
  },
}

// Topics API
export const topicsAPI = {
  getAll: async (): Promise<Topic[]> => {
    try {
      const data = await makeRequest("/topics/")
      // Handle both array and paginated response
      const topics = Array.isArray(data) ? data : data.results || []
      
      return topics.map((topic: any) => ({
        id: topic.id.toString(),
        name: topic.name,
        description: topic.description,
        color: topic.color,
        vocabularyCount: topic.vocabulary_count || 0,
        createdAt: topic.created_at,
      }))
    } catch (error) {
      console.error("Error fetching topics:", error)
      throw error
    }
  },

  create: async (topic: Omit<Topic, "id" | "vocabularyCount" | "createdAt">) => {
    const data = await makeRequest("/topics/", {
      method: "POST",
      body: JSON.stringify({
        name: topic.name,
        description: topic.description,
        color: topic.color,
      }),
    })

    return {
      id: data.id.toString(),
      name: data.name,
      description: data.description,
      color: data.color,
      vocabularyCount: data.vocabulary_count,
      createdAt: data.created_at,
    }
  },

  update: async (id: string, topic: Partial<Topic>) => {
    const data = await makeRequest(`/topics/${id}/`, {
      method: "PATCH",
      body: JSON.stringify({
        name: topic.name,
        description: topic.description,
        color: topic.color,
      }),
    })

    return {
      id: data.id.toString(),
      name: data.name,
      description: data.description,
      color: data.color,
      vocabularyCount: data.vocabulary_count,
      createdAt: data.created_at,
    }
  },

  delete: async (id: string) => {
    await makeRequest(`/topics/${id}/`, {
      method: "DELETE",
    })
    return { success: true }
  },
}

// Vocabulary API
export const vocabularyAPI = {
  getByTopic: async (topicId: string): Promise<Vocabulary[]> => {
    const data = await makeRequest(`/vocabulary/topic/${topicId}/`)
    return data.map((vocab: any) => ({
      id: vocab.id.toString(),
      topicId: vocab.topic_id?.toString() || topicId,
      word: vocab.word,
      pronunciation: vocab.pronunciation,
      meaning: vocab.meaning,
      example: vocab.example,
      difficulty: vocab.difficulty,
    }))
  },

  create: async (vocabulary: Omit<Vocabulary, "id">) => {
    const data = await makeRequest("/vocabulary/", {
      method: "POST",
      body: JSON.stringify({
        topic_id: Number.parseInt(vocabulary.topicId),
        word: vocabulary.word,
        pronunciation: vocabulary.pronunciation,
        meaning: vocabulary.meaning,
        example: vocabulary.example,
        difficulty: vocabulary.difficulty,
      }),
    })

    return {
      id: data.id.toString(),
      topicId: data.topic_id?.toString() || vocabulary.topicId,
      word: data.word,
      pronunciation: data.pronunciation,
      meaning: data.meaning,
      example: data.example,
      difficulty: data.difficulty,
    }
  },

  update: async (id: string, vocabulary: Partial<Vocabulary>) => {
    const updateData: any = {}
    if (vocabulary.word) updateData.word = vocabulary.word
    if (vocabulary.pronunciation) updateData.pronunciation = vocabulary.pronunciation
    if (vocabulary.meaning) updateData.meaning = vocabulary.meaning
    if (vocabulary.example) updateData.example = vocabulary.example
    if (vocabulary.difficulty) updateData.difficulty = vocabulary.difficulty

    const data = await makeRequest(`/vocabulary/${id}/`, {
      method: "PATCH",
      body: JSON.stringify(updateData),
    })

    return {
      id: data.id.toString(),
      topicId: data.topic_id?.toString(),
      word: data.word,
      pronunciation: data.pronunciation,
      meaning: data.meaning,
      example: data.example,
      difficulty: data.difficulty,
    }
  },

  delete: async (id: string) => {
    await makeRequest(`/vocabulary/${id}/`, {
      method: "DELETE",
    })
    return { success: true }
  },
}

// Progress API
export const progressAPI = {
  getUserProgress: async (userId: string, topicId: string): Promise<UserProgress[]> => {
    const data = await makeRequest(`/progress/${userId}/${topicId}/`)
    return data.map((progress: any) => ({
      id: progress.id,
      userId: progress.userId.toString(),
      topicId: progress.topicId.toString(),
      vocabularyId: progress.vocabularyId.toString(),
      status: progress.status,
      correctCount: progress.correctCount,
      totalAttempts: progress.totalAttempts,
      lastStudied: progress.lastStudied,
    }))
  },

  updateProgress: async (progress: Partial<UserProgress>) => {
    await makeRequest("/progress/update/", {
      method: "POST",
      body: JSON.stringify({
        userId: progress.userId,
        topicId: progress.topicId,
        vocabularyId: progress.vocabularyId,
        status: progress.status,
        correctCount: progress.correctCount,
        totalAttempts: progress.totalAttempts,
      }),
    })
    return { success: true }
  },
}
