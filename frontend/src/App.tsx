import { useState } from "react";
import { askQuestion } from "./api";

function App() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState<number[]>([]);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!query) return;

    setLoading(true);
    const res = await askQuestion(query);
    setAnswer(res.answer);
    //setSources(res.sources);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="w-full max-w-2xl bg-white rounded-xl shadow-md p-6">
        <h1 className="text-2xl font-bold mb-4 text-center">
          📄 Chat with My Resume
        </h1>

        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask about skills, experience, projects..."
          className="w-full border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        <button
          onClick={handleAsk}
          className="mt-4 w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition"
        >
          Ask
        </button>

        {loading && (
          <p className="mt-4 text-center text-gray-500">Thinking…</p>
        )}

        {answer && (
          <div className="mt-6">
            <h3 className="font-semibold text-lg mb-2">Answer</h3>
            <p className="text-gray-800 whitespace-pre-line">{answer}</p>

            <h4 className="font-semibold mt-4">Sources</h4>
            <ul className="list-disc list-inside text-sm text-gray-600">
              {sources.map((s, i) => (
                <li key={i}>Page {s}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
