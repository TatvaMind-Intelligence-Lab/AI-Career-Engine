import { useState } from "react";
import UploadForm from "../Components/UploadForm";
import ResultCard from "../Components/ResultCard";

export default function Home() {
  const [result, setResult] = useState(null);
  const [retrieval, setRetrieval] = useState([]);

  return (
    <div className="min-h-screen bg-gray-100 p-6 flex flex-col items-center">
      
      <h1 className="text-3xl font-bold mb-6">
        TatvaMind AI Career Engine
      </h1>

      <div className="w-full max-w-2xl">
        <UploadForm 
          setResult={setResult} 
          setRetrieval={setRetrieval} 
        />

        <ResultCard 
          data={result} 
          retrieval={retrieval} 
        />
      </div>

    </div>
  );
}