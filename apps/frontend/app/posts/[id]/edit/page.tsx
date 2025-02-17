"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { getPost, updatePost } from "@/lib/api";
import PostForm from "@/components/post-form";
import { useToast } from "@/hooks/use-toast";

export default function EditPost({ params }: { params: { id: string } }) {
  const [post, setPost] = useState<{ title: string; content: string } | null>(
    null
  );
  const [isSubmitting, setIsSubmitting] = useState(false);
  const router = useRouter();
  const { toast } = useToast();

  useEffect(() => {
    const loadPost = async () => {
      try {
        const data = await getPost(params.id);
        setPost(data);
      } catch (error) {
        toast({
          title: "Error",
          description: "Failed to load post",
          variant: "destructive",
        });
        router.push("/");
      }
    };
    loadPost();
  }, [params.id, router, toast]);

  const handleSubmit = async (data: { title: string; content: string }) => {
    setIsSubmitting(true);
    try {
      await updatePost(params.id, data);
      toast({
        title: "Success",
        description: "Post updated successfully",
      });
      router.push("/");
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to update post",
        variant: "destructive",
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  if (!post) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold tracking-tight mb-8">Edit Post</h1>
      <PostForm
        initialData={post}
        onSubmit={handleSubmit}
        isSubmitting={isSubmitting}
      />
    </div>
  );
}
