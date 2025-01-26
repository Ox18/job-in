import { ref } from "vue";
import { useJobApi } from "./useJobApi";

export const useMainView = () => {
  const jobApi = useJobApi();

  const jobs = ref([]);
  const isLoading = ref(false);

  const pagination = ref({
    total_items: 0,
    limit: 0,
    start: 0,
    page: 0,
    total_pages: 0,
  });

  const load = async (page = 1) => {
    isLoading.value = true;
    try {
      const { data } = await jobApi.getJobs(page);
      jobs.value = data.jobs;
      pagination.value = data.pagination;
    } catch (ex) {
      console.error(ex);
    } finally {
      isLoading.value = false;
    }
  };

  return {
    load,
    jobs,
    isLoading,
  };
};
