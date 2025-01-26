import { ref } from "vue";
import { useJobApi } from "./useJobApi";

export const useFindView = () => {
  const jobApi = useJobApi();

  const page = ref(0);
  const isLoading = ref(false);
  const job = ref(null);
  const jobs = ref([]);
  const feedback = ref(null);

  const loadFeedback = async () => {
    const response = await jobApi.feedback(job.value.post_id);
    feedback.value = response.data.feedback_data;
  };

  const next = async (remove = false) => {
    isLoading.value = true;

    if (remove) {
      jobs.value = jobs.value.filter(
        (item) => item.post_id !== job.value.post_id
      );
    }

    if (jobs.value.length === 0) {
      page.value = page.value + 1;

      while (jobs.value.length === 0) {
        const response = await jobApi.getJobs(page.value);

        jobs.value = response.data.jobs.filter(
          (item) => item.status !== "APPLIED"
        );
      }
    }

    const random = Math.floor(Math.random() * jobs.value.length);
    job.value = jobs.value[random];
    loadFeedback();
    isLoading.value = false;
  };

  next();

  const open = () => {
    const width = 1200;
    const height = 1200;

    // Calcula la posición centrada
    const left = (window.screen.width - width) / 2;
    const top = (window.screen.height - height) / 2;

    // Abre la ventana emergente
    const popup = window.open(
      "https://www.linkedin.com/jobs/view/" + job.value.post_id,
      "LinkedIn Job",
      `width=${width},height=${height},top=${top},left=${left}`
    );

    // Verifica si el popup se abrió correctamente
    if (!popup || popup.closed || typeof popup.closed === "undefined") {
      alert("Por favor, habilita los popups para este sitio.");
    }
  };

  const save = async () => {
    try {
      if (job.value) {
        await jobApi.save(job.value);
        await next(true);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const reject = async () => {
    try {
      if (job.value) {
        await jobApi.reject(job.value);
        await next(true);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return {
    next,
    job,
    isLoading,
    open,
    save,
    reject,
    feedback,
  };
};
