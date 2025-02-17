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

export const getPost = async (id: string): Promise<Post> => {
  const response = await api.get(`/posts/${id}`);
  return response.data;
};

export const createPost = async (
  post: Omit<Post, "id" | "created_at">
): Promise<Post> => {
  console.log(post);
  const response = await api.post("/posts/", post);
  return response.data;
};

export const updatePost = async (
  id: string,
  post: Partial<Post>
): Promise<Post> => {
  const response = await api.put(`/posts/${id}`, post);
  return response.data;
};

export const deletePost = async (id: string): Promise<void> => {
  await api.delete(`/posts/${id}`);
};
