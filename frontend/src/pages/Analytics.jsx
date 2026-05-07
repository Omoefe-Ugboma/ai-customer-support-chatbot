import { useEffect, useState } from "react";

import Layout from "../components/Layout";

import {
  getSummary,
  getRecent,
} from "../services/analyticsService";

export default function Analytics() {

  const [summary, setSummary] = useState(null);

  const [recent, setRecent] = useState([]);

  useEffect(() => {

    async function loadData() {

      const summaryData =
        await getSummary();

      const recentData =
        await getRecent();

      setSummary(summaryData);

      setRecent(recentData);
    }

    loadData();

  }, []);

  return (
    <Layout>

      <h1 className="text-3xl font-bold mb-6">
        Analytics
      </h1>

      {summary && (

        <div className="grid grid-cols-3 gap-4 mb-8">

          <div className="bg-slate-900 p-6 rounded-lg">
            <h2>Total Requests</h2>

            <p className="text-3xl">
              {summary.total_requests}
            </p>
          </div>

          <div className="bg-slate-900 p-6 rounded-lg">
            <h2>Average Response</h2>

            <p className="text-3xl">
              {summary.avg_response_time}
            </p>
          </div>

        </div>
      )}

      <div className="bg-slate-900 p-6 rounded-lg">

        <h2 className="text-2xl mb-4">
          Recent Chats
        </h2>

        {recent.map((item, index) => (

          <div
            key={index}
            className="border-b border-slate-700 py-4"
          >
            <p>
              <strong>Question:</strong>{" "}
              {item.question}
            </p>

            <p>
              <strong>Response:</strong>{" "}
              {item.response}
            </p>

          </div>

        ))}

      </div>

    </Layout>
  );
}