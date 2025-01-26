import axios from "axios";

export const useJobApi = () => {
  const getJobs = async (page) => {
    const response = await fetch(`http://localhost:8000/jobs?page=${page}`);

    if (!response.ok) {
      throw new Error("Failed to fetch jobs");
    }

    return await response.json();
  };

  const save = async (job) => {
    const response = await axios.post("http://localhost:8000/jobs/save", job);

    return response.data;
  };

  const reject = async (job) => {
    const response = await axios.post("http://localhost:8000/jobs/reject", job);

    return response.data;
  };

  const feedback = async (post_id) => {
    const response = await axios.get(
      "http://localhost:8000/jobs/feedback?post_id=" + post_id
    );

    return response.data;
  };

  return {
    feedback,
    getJobs,
    save,
    reject,
  };
};
