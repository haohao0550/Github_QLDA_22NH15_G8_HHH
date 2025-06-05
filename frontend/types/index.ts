export interface User {
  id: string
  email: string
  name: string
  role: "admin" | "user"
}

export interface Admin {
  id: string
  email: string
  name: string
  role: "admin"
}

export interface RegularUser {
  id: string
  email: string
  name: string
  role: "user"
}

export interface Topic {
  id: string
  name: string
  description: string
  color: string
  vocabularyCount: number
  createdAt: string
}

export interface Vocabulary {
  id: string
  topicId: string
  word: string
  pronunciation: string
  meaning: string
  example: string
  imageUrl?: string
  difficulty: "easy" | "medium" | "hard"
}

export interface UserProgress {
  id: string
  userId: string
  topicId: string
  vocabularyId: string
  status: "learning" | "mastered" | "review"
  correctCount: number
  totalAttempts: number
  lastStudied: string
}

export interface FlashCard {
  vocabulary: Vocabulary
  isFlipped: boolean
}
