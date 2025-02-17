import { Suspense } from "react";
import BlogPosts from "@/components/blog-posts";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import { PlusCircle } from "lucide-react";

export default function Home() {
  return (
    <main className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold tracking-tight">
          Blog Posts Manager
        </h1>
        <Link href="/posts/new">
          <Button>
            <PlusCircle className="mr-2 h-4 w-4" />
            New Post
          </Button>
        </Link>
      </div>
      <Suspense fallback={<div>Loading posts...</div>}>
        <BlogPosts />
      </Suspense>
    </main>
  );
}
