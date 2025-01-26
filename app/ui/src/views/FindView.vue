<script>
import { useFindView } from "@/composables/useFindView";
import Card from "@/components/Card.vue";
import Feedback from "@/components/Feedback.vue";

export default {
  name: "FindView",
  components: {
    Card,
    Feedback,
  },
  setup() {
    const { job, isLoading, open, save, reject, next, feedback } = useFindView();
    return {
      job,
      next,
      isLoading,
      open,
      save,
      reject,
      feedback,
    };
  },
  methods: {
    onCardExpired() {
      this.next();
      console.log("executed");
    },
    onOpen() {
      this.open();
    },
    async onAccept() {
      await this.save();
    },
    async onReject() {
      await this.reject();
    },
    onSeeLater() {
      this.next();
    },
  },
};
</script>

<template>
  <div class="flex justify-center items-center h-screen">
    <div
      v-if="job"
      class="grid grid-cols-2 gap-10 w-full max-w-[800px] justify-center items-center"
    >
      <div>
        <Card
          class="w-full"
          :key="job.post_id"
          :job="job"
          :loading="isLoading"
          @expired="onCardExpired"
          @open="onOpen"
          @accept="onAccept"
          @reject="onReject"
          @see-later="onSeeLater"
        />
      </div>
      <Feedback v-if="feedback" v-model="feedback" />
    </div>
  </div>
</template>
