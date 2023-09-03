<template>
    <!-- Modal -->
    <div class="modal fade" id="alertPopup" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Error</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    {{ errorcontent }}
                </div>
            </div>
        </div>
    </div>
    <!-- Modal -->
</template>

<script>
export default {
    props: {
        errorcontent: String, // Przekazuje zawartość błędu jako props
    },
};
</script>
