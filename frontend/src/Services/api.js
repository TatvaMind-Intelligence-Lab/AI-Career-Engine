export async function analyzeResume(file, jd) {
  const formData = new FormData();

  formData.append("resume", file);
  formData.append("job_description", jd);

  const res = await fetch("http://localhost:8000/api/v1/analyze", {
    method: "POST",
    body: formData,
  });

  return res.json();
}