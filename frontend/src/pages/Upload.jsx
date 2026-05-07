import { useState } from "react";

import Layout from "../components/Layout";

import {
  uploadDocument,
  resetDocuments,
  clearCache,
} from "../services/documentService";

export default function Upload() {

  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {

    if (!file) return;

    setLoading(true);

    try {

      await uploadDocument(file);

      alert("Document uploaded successfully");

    } catch (error) {

      console.error(error);

      alert("Upload failed");

    } finally {

      setLoading(false);

    }

  };

  return (
    <Layout>

      <div className="max-w-3xl">

        <h1 className="text-4xl font-bold mb-2">
          Upload Documents
        </h1>

        <p className="text-slate-400 mb-8">
          Upload PDF or TXT files for AI retrieval.
        </p>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

          <input
            type="file"
            onChange={(e) =>
              setFile(e.target.files[0])
            }
            className="mb-6"
          />

          <div className="flex flex-wrap gap-4">

            <button
              onClick={handleUpload}
              className="bg-blue-600 px-5 py-3 rounded-xl"
            >
              {loading
                ? "Uploading..."
                : "Upload"}
            </button>

            <button
              onClick={resetDocuments}
              className="bg-yellow-600 px-5 py-3 rounded-xl"
            >
              Reset Documents
            </button>

            <button
              onClick={clearCache}
              className="bg-red-600 px-5 py-3 rounded-xl"
            >
              Clear Cache
            </button>

          </div>

        </div>

      </div>

    </Layout>
  );
}