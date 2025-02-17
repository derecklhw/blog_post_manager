import axios from "axios";

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
});

export interface Post {
  id: string;
  title: string;
  content: string;
  created_at: string;
}

export const getPosts = async (): Promise<Post[]> => {
  const response = await api.get("/posts");
  return response.data;
};
