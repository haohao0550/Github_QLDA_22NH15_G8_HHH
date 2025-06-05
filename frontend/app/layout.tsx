import { PublicNavbar } from "@/components/layout/public-navbar"
import { Toaster } from "@/components/ui/toaster"
import { AuthProvider } from "@/contexts/auth-context"
import type { Metadata } from "next"
import { Inter } from "next/font/google"
import type React from "react"
import "./globals.css"

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "Wordify - English Vocabulary Learning",
  description: "Master English vocabulary with interactive flashcards and topic-based learning",
  generator: 'v0.dev'
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AuthProvider>
          <PublicNavbar />
          {children}
          <Toaster />
        </AuthProvider>
      </body>
    </html>
  )
}
