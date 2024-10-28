<template>
  <Teleport to="body">
    <div
      class="modal modal-sheet position-absolute d-block bg-body-secondary p-4 py-md-5"
      tabindex="-1"
      role="dialog"
      id="modalSheet"
      v-if="show"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content rounded-4 shadow">
          <div class="modal-header border-bottom-0">
            <h1 class="modal-title fs-5">{{ title }}</h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
              @click="emits('close-modal')"
            ></button>
          </div>
          <div class="modal-body py-0">
            <p>
              {{ message }}
            </p>
          </div>
          <div
            class="modal-footer flex-column align-items-stretch w-100 gap-2 pb-3 border-top-0"
          >
            <button type="button" class="btn btn-lg btn-primary">
              Save changes
            </button>
            <button
              type="button"
              class="btn btn-lg btn-secondary"
              data-bs-dismiss="modal"
              @click="emits('close-modal')"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup>
const props = defineProps({
  message: String,
  title: String,
  show: { type: Boolean, default: false },
});

const emits = defineEmits(["close-modal"]);
</script>

<style>
.modal-sheet .modal-dialog {
  width: 380px;
  transition: bottom 0.75s ease-in-out;
}
.modal-sheet .modal-footer {
  padding-bottom: 2rem;
}
</style>
