import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import { generateLovePlan } from './api'

function App() {
  const [story, setStory] = useState('')
  const [plan, setPlan] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleGenerate = async () => {
    if (!story.trim()) {
      setError("Please tell us your story first!")
      return
    }

    setLoading(true)
    setError('')
    setPlan('')

    try {
      const result = await generateLovePlan(story)
      setPlan(result)
    } catch (err) {
      setError(err.message || 'Failed to connect to the love experts.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <header className="app-header">
        <h1 className="logo-text">LoveGPT Tamil</h1>
        <p className="subtitle">Ungala love story sollunga — perfect plan ready pannuvom 🌹</p>
      </header>

      <main className="main-grid">
        <section className="input-section glass-card">
          <label className="input-label" htmlFor="story-input">
            <span>💬</span> Ungala Love Story
          </label>
          <textarea
            id="story-input"
            className="story-textarea"
            placeholder="Example: Naan oru ponnaiya college-la paarthen, ava per Priya, aana pesave mudiyala..."
            value={story}
            onChange={(e) => {
              setStory(e.target.value)
              if (error) setError('')
            }}
          />

          {error && <div style={{ color: '#ff7b54', fontSize: '0.9rem' }}>{error}</div>}

          <button
            className="btn btn-primary"
            onClick={handleGenerate}
            disabled={loading}
          >
            {loading ? (
              <>
                <div className="loader"></div>
                Analyzing Emotions...
              </>
            ) : (
              <>🚀 Love Plan Uruvaakku</>
            )}
          </button>

          <div className="tips-container">
            <h4>💡 Tips for best results:</h4>
            <ul>
              <li>Ungala story detailed-a sollunga.</li>
              <li>Ava peyar, place, situation ellame include pannunga.</li>
              <li>Tamil or English — you can use any language.</li>
            </ul>
          </div>
        </section>

        <section className="output-section glass-card">
          <h2 className="output-header">📋 Your Personalized Plan</h2>

          <div className="plan-content">
            {loading ? (
              <div className="plan-empty">
                <div className="loader" style={{ width: '40px', height: '40px', borderWidth: '4px' }}></div>
                <p>Our 10 AI Agents are analyzing your story and crafting a master plan...</p>
              </div>
            ) : plan ? (
              <ReactMarkdown>{plan}</ReactMarkdown>
            ) : (
              <div className="plan-empty">
                <div className="empty-icon">💌</div>
                <p>Your step-by-step master plan will appear here.</p>
              </div>
            )}
          </div>
        </section>
      </main>
    </div>
  )
}

export default App
