import axios from "axios";

//const API_URL = "https://resume-rag-backend.onrender.com";
const API_URL = "http://127.0.0.1:8000";

export const askQuestion = async (query: string) => {
  const response = await axios.post(`${API_URL}/ask`, { query });
  return response.data;
};
