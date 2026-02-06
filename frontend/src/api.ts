import axios from "axios";

const API_URL = "https://rag-chat-llm.onrender.com";
//const API_URL = "http://127.0.0.1:8000";

export const askQuestion = async (query: string) => {
  const response = await axios.post(
    `${API_URL}/ask`,
    { query },
    { timeout: 15000 } // ⏱ 15 seconds
  );
  return response.data;
};
