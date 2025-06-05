"use client"

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/contexts/auth-context"
import { TopicManagement } from "@/components/admin/topic-management"
import { TopicSelection } from "@/components/user/topic-selection"
import { LearningSession } from "@/components/learning/learning-session"
import type { Topic } from "@/types"

export default function DashboardPage() {
  const { user, loading } = useAuth()
  const router = useRouter()
  const [selectedTopic, setSelectedTopic] = useState<Topic | null>(null)

  useEffect(() => {
    if (!user && !loading) {
      router.push("/login")
    }
  }, [user, loading, router])

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-2 text-gray-600">Loading...</p>
        </div>
      </div>
    )
  }

  if (!user) {
    return null // Will redirect to login
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <main className="container mx-auto px-4 py-8">
        {user.role === "admin" ? (
          <div className="space-y-6">
            <div className="bg-white rounded-lg shadow-sm p-6">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">Admin Dashboard</h1>
              <p className="text-gray-600">Manage topics and vocabulary for all users</p>
            </div>
            <TopicManagement />
          </div>
        ) : selectedTopic ? (
          <LearningSession topic={selectedTopic} onBack={() => setSelectedTopic(null)} />
        ) : (
          <div className="space-y-6">
            <div className="bg-white rounded-lg shadow-sm p-6">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">Welcome back, {user.name}!</h1>
              <p className="text-gray-600">Continue your vocabulary learning journey</p>
            </div>
            <TopicSelection onSelectTopic={setSelectedTopic} />
          </div>
        )}
      </main>
    </div>
  )
}
