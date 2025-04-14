# Terraform Configuration Template for GCS Storage

variable "CLUSTER_NAME" {
  description = "The name of the cluster"
  type        = string
}

resource "google_storage_bucket" "bucket" {
  name     = "${var.CLUSTER_NAME}-bucket"
  location = "US"
}