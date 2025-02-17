'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { createPost } from '@/lib/api';
import PostForm from '@/components/post-form';
import { useToast } from '@/hooks/use-toast';

export default function NewPost() {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const router = useRouter();
  const { toast } = useToast();

  const handleSubmit = async (data: { title: string; content: string }) => {
    setIsSubmitting(true);
    try {
      await createPost(data);
      toast({
        title: 'Success',
        description: 'Post created successfully',
      });
      router.push('/');
    } catch (error) {
      toast({
        title: 'Error',
        description: 'Failed to create post',
        variant: 'destructive',
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold tracking-tight mb-8">Create New Post</h1>
      <PostForm onSubmit={handleSubmit} isSubmitting={isSubmitting} />
    </div>
  );
}