import { useEffect, useRef, useState } from "react"
import ReactMarkdown from "react-markdown"
import toast, { Toaster } from "react-hot-toast"

import API from "./services/api"


type Message = {
  role: "user" | "assistant"
  content: string
  sources?: any[]
}


export default function App() {

  const [repoUrl, setRepoUrl] = useState("")
  const [question, setQuestion] = useState("")
  const [messages, setMessages] = useState<Message[]>([])
  const [indexing, setIndexing] = useState(false)
  const [asking, setAsking] = useState(false)

  const chatContainerRef = useRef<HTMLDivElement>(null)


  useEffect(() => {

    if (chatContainerRef.current) {

      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight
    }

  }, [messages])


  async function indexRepository() {

    if (!repoUrl.trim()) return

    try {

      setIndexing(true)

      await API.post("/index", {
        repo_url: repoUrl
      })

      toast.success("Repository indexed successfully!")

    } catch (error) {

      console.error(error)

      toast.error("Failed to index repository")

    } finally {

      setIndexing(false)
    }
  }


  async function askQuestion() {

    if (!question.trim()) return
  
    const userMessage: Message = {
      role: "user",
      content: question
    }
  
    setMessages((prev) => [
      ...prev,
      userMessage
    ])
  
    const currentQuestion = question
  
    setQuestion("")
  
    try {
  
      setAsking(true)
  
      const response = await fetch(
        "http://localhost:8000/ask-stream",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            question: currentQuestion
          })
        }
      )
  
      if (!response.body) {
  
        throw new Error("No response body")
      }
  
      const reader = response.body.getReader()
  
      const decoder = new TextDecoder()
  
      let streamedText = ""
  
      const assistantMessage: Message = {
        role: "assistant",
        content: ""
      }
  
      setMessages((prev) => [
        ...prev,
        assistantMessage
      ])
  
      while (true) {
  
        const { done, value } =
          await reader.read()
  
        if (done) break
  
        streamedText += decoder.decode(value)
  
        setMessages((prev) => {
  
          const updated = [...prev]
  
          updated[updated.length - 1] = {
            role: "assistant",
            content: streamedText
          }
  
          return updated
        })
      }
  
    } catch (error) {
  
      console.error(error)
  
      toast.error("Failed to ask question")
  
    } finally {
  
      setAsking(false)
    }
  }


  return (

    <div className="min-h-screen bg-slate-950 text-white">

      <Toaster position="top-right" />

      <div className="max-w-5xl mx-auto p-8">

        <h1 className="text-5xl font-bold mb-3">
          RepoMind
        </h1>

        <p className="text-slate-400 text-lg mb-10">
          AI-powered repository intelligence platform
        </p>


        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl mb-6">

          <h2 className="text-2xl font-semibold mb-4">
            Index Repository
          </h2>

          <div className="flex gap-4">

            <input
              type="text"
              placeholder="https://github.com/user/repo"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
              onKeyDown={(e) => {

                if (e.key === "Enter") {

                  indexRepository()
                }
              }}
              className="flex-1 p-4 rounded-xl bg-slate-800 text-white border border-slate-700 outline-none focus:border-blue-500"
            />

            <button
              onClick={indexRepository}
              className="bg-blue-600 hover:bg-blue-700 transition-all px-6 rounded-xl font-semibold"
            >
              {indexing ? "Indexing..." : "Index"}
            </button>

          </div>

        </div>


        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

          <div
            ref={chatContainerRef}
            className="space-y-6 mb-6 max-h-[600px] overflow-y-auto pr-2"
          >

            {messages.map((message, index) => (

              <div
                key={index}
                className={`flex ${
                  message.role === "user"
                    ? "justify-end"
                    : "justify-start"
                }`}
              >

                <div
                  className={`max-w-3xl p-5 rounded-2xl ${
                    message.role === "user"
                      ? "bg-blue-600"
                      : "bg-slate-800 border border-slate-700"
                  }`}
                >

                  <div className="prose prose-invert max-w-none">

                    <ReactMarkdown>
                      {message.content}
                    </ReactMarkdown>

                  </div>


                  {message.sources && (

                    <div className="mt-5">

                      <p className="text-sm text-slate-400 mb-2">
                        Sources
                      </p>

                      <div className="space-y-2">

                        {message.sources.map((source, sourceIndex) => (

                          <div
                            key={sourceIndex}
                            className="bg-slate-900 p-3 rounded-xl text-sm border border-slate-700"
                          >

                            <p className="font-medium break-all">
                              {source.path}
                            </p>

                            <p className="text-slate-400 mt-1">
                              Score: {source.score}
                            </p>

                          </div>
                        ))}

                      </div>

                    </div>
                  )}

                </div>

              </div>
            ))}

          </div>


          <div className="flex gap-4">

            <input
              type="text"
              placeholder="Ask RepoMind anything..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => {

                if (e.key === "Enter") {

                  askQuestion()
                }
              }}
              className="flex-1 p-4 rounded-xl bg-slate-800 text-white border border-slate-700 outline-none focus:border-emerald-500"
            />

            <button
              onClick={askQuestion}
              className="bg-emerald-600 hover:bg-emerald-700 transition-all px-6 rounded-xl font-semibold"
            >
              {asking ? "Thinking..." : "Ask"}
            </button>

          </div>

        </div>

      </div>

    </div>
  )
}