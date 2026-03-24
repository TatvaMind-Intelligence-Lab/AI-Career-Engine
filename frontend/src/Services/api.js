const BASE_URL = "http://127.0.0.1:8000/api/v1";

export async function authorizedFetch(endpoint, options = {}) {
  const token = localStorage.getItem("token");

  const url = `http://127.0.0.1:8000/api/v1${endpoint}`; // 🔥 force absolute


  const res = await fetch(url, {
    ...options,
    headers: {
      ...(token && { Authorization: `Bearer ${token}` }),
      ...(options.headers || {}),
    },
  });

  const data = await res.json();

  if (!res.ok) throw data;

  return data;
}

// ✅ ANALYZE FUNCTION
export async function analyzeResume(file, jd) {
  const formData = new FormData();

  formData.append("resume", file);
  formData.append("job_description", jd);

  return authorizedFetch("/analyze", {
    method: "POST",
    body: formData,
  });
}
