"use client"

import { useState, useEffect } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import type { Topic, UserProgress } from "@/types"
import { topicsAPI, progressAPI } from "@/lib/api"
import { useAuth } from "@/contexts/auth-context"
import { BookOpen, Play, Trophy, Target, TrendingUp } from "lucide-react"

interface TopicSelectionProps {
  onSelectTopic: (topic: Topic) => void
}

export function TopicSelection({ onSelectTopic }: TopicSelectionProps) {
  const [topics, setTopics] = useState<Topic[]>([])
  const [progress, setProgress] = useState<Record<string, UserProgress[]>>({})
  const [loading, setLoading] = useState(true)
  const { user } = useAuth()

  useEffect(() => {
    loadData()
  }, [user])

  const loadData = async () => {
    try {
      const topicsData = await topicsAPI.getAll()
      setTopics(topicsData)

      if (user) {
        const progressData: Record<string, UserProgress[]> = {}
        for (const topic of topicsData) {
          progressData[topic.id] = await progressAPI.getUserProgress(user.id, topic.id)
        }
        setProgress(progressData)
      }
    } catch (error) {
      console.error("Failed to load data:", error)
    } finally {
      setLoading(false)
    }
  }

  const getTopicProgress = (topicId: string) => {
    const topicProgress = progress[topicId] || []
    const masteredCount = topicProgress.filter((p) => p.status === "mastered").length
    const learningCount = topicProgress.filter((p) => p.status === "learning").length
    const totalCount = topicProgress.length
    return {
      masteredCount,
      learningCount,
      totalCount,
      percentage: totalCount > 0 ? (masteredCount / totalCount) * 100 : 0,
    }
  }

  const getProgressStatus = (percentage: number) => {
    if (percentage === 0) return { label: "Start Learning", color: "text-gray-500", bgColor: "bg-gray-100" }
    if (percentage < 30) return { label: "Beginner", color: "text-red-600", bgColor: "bg-red-100" }
    if (percentage < 70) return { label: "Learning", color: "text-yellow-600", bgColor: "bg-yellow-100" }
    if (percentage < 100) return { label: "Advanced", color: "text-blue-600", bgColor: "bg-blue-100" }
    return { label: "Mastered", color: "text-green-600", bgColor: "bg-green-100" }
  }

  const getTotalStats = () => {
    const totalMastered = Object.values(progress).reduce(
      (acc, topicProgress) => acc + topicProgress.filter((p) => p.status === "mastered").length,
      0,
    )
    const totalLearning = Object.values(progress).reduce(
      (acc, topicProgress) => acc + topicProgress.filter((p) => p.status === "learning").length,
      0,
    )
    const totalWords = Object.values(progress).reduce((acc, topicProgress) => acc + topicProgress.length, 0)
    const overallProgress = totalWords > 0 ? Math.round((totalMastered / totalWords) * 100) : 0

    return { totalMastered, totalLearning, totalWords, overallProgress }
  }

  if (loading) {
    return (
      <div className="flex justify-center items-center p-12">
        <div className="text-center space-y-4">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="text-gray-600 font-medium">Loading your learning dashboard...</p>
        </div>
      </div>
    )
  }

  const stats = getTotalStats()

  return (
    <div className="space-y-8">
      {/* Welcome Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Welcome back, {user?.name}!</h2>
        <p className="text-gray-600 text-lg">Continue your vocabulary learning journey</p>
      </div>

      {/* Stats Overview */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="bg-gradient-to-r from-blue-500 to-blue-600 text-white border-0">
          <CardContent className="p-4">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-white/20 rounded-lg">
                <BookOpen className="h-6 w-6" />
              </div>
              <div>
                <div className="text-2xl font-bold">{topics.length}</div>
                <div className="text-blue-100 text-sm">Available Topics</div>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="bg-gradient-to-r from-green-500 to-green-600 text-white border-0">
          <CardContent className="p-4">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-white/20 rounded-lg">
                <Trophy className="h-6 w-6" />
              </div>
              <div>
                <div className="text-2xl font-bold">{stats.totalMastered}</div>
                <div className="text-green-100 text-sm">Words Mastered</div>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="bg-gradient-to-r from-purple-500 to-purple-600 text-white border-0">
          <CardContent className="p-4">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-white/20 rounded-lg">
                <Target className="h-6 w-6" />
              </div>
              <div>
                <div className="text-2xl font-bold">{stats.totalLearning}</div>
                <div className="text-purple-100 text-sm">In Progress</div>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="bg-gradient-to-r from-orange-500 to-orange-600 text-white border-0">
          <CardContent className="p-4">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-white/20 rounded-lg">
                <TrendingUp className="h-6 w-6" />
              </div>
              <div>
                <div className="text-2xl font-bold">{stats.overallProgress}%</div>
                <div className="text-orange-100 text-sm">Overall Progress</div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Topics Grid */}
      <div>
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-2xl font-bold text-gray-900">Choose Your Learning Path</h3>
          <Badge variant="outline" className="text-sm">
            {topics.length} topics available
          </Badge>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {topics.map((topic) => {
            const { masteredCount, learningCount, totalCount, percentage } = getTopicProgress(topic.id)
            const status = getProgressStatus(percentage)

            return (
              <Card
                key={topic.id}
                className="hover:shadow-xl transition-all duration-300 hover:scale-[1.02] border-l-4 group cursor-pointer"
                style={{ borderLeftColor: topic.color }}
                onClick={() => onSelectTopic(topic)}
              >
                <CardHeader className="pb-3">
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center space-x-2">
                      <div className="w-3 h-3 rounded-full" style={{ backgroundColor: topic.color }} />
                      <CardTitle className="text-lg font-bold">{topic.name}</CardTitle>
                    </div>
                    <Badge className={`${status.bgColor} ${status.color} border-0 text-xs font-medium`}>
                      {status.label}
                    </Badge>
                  </div>
                  <CardDescription className="text-sm leading-relaxed line-clamp-2">
                    {topic.description}
                  </CardDescription>
                </CardHeader>

                <CardContent className="space-y-4">
                  {/* Stats */}
                  <div className="grid grid-cols-3 gap-2 text-center">
                    <div className="bg-gray-50 rounded-lg p-2">
                      <div className="text-lg font-bold text-gray-900">{topic.vocabularyCount}</div>
                      <div className="text-xs text-gray-600">Total</div>
                    </div>
                    <div className="bg-green-50 rounded-lg p-2">
                      <div className="text-lg font-bold text-green-600">{masteredCount}</div>
                      <div className="text-xs text-green-700">Mastered</div>
                    </div>
                    <div className="bg-yellow-50 rounded-lg p-2">
                      <div className="text-lg font-bold text-yellow-600">{learningCount}</div>
                      <div className="text-xs text-yellow-700">Learning</div>
                    </div>
                  </div>

                  {/* Progress Bar */}
                  {percentage > 0 && (
                    <div className="space-y-2">
                      <div className="flex justify-between text-sm">
                        <span className="text-gray-600">Progress</span>
                        <span className="font-medium">{Math.round(percentage)}%</span>
                      </div>
                      <Progress value={percentage} className="h-2" />
                    </div>
                  )}

                  {/* Action Button */}
                  <Button
                    className="w-full group-hover:shadow-md transition-all duration-200 font-medium"
                    style={{ backgroundColor: topic.color }}
                  >
                    <Play className="mr-2 h-4 w-4" />
                    {percentage === 0 ? "Start Learning" : percentage === 100 ? "Review Words" : "Continue Learning"}
                  </Button>
                </CardContent>
              </Card>
            )
          })}
        </div>
      </div>
    </div>
  )
}
