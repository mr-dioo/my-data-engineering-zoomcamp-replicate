terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.20.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project = "ha-do-terraform-practice"
  region  = var.service_region
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "ha-saves-in-bucket"
  location      = var.service_location
  force_destroy = true
  storage_class = "STANDARD"


  lifecycle_rule {
    condition {
      age = 1
    }

    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id                  = "ha_has_dataset"
  friendly_name               = "bqdb"
  description                 = "This is a test dataset to store my practice"
  location                    = var.service_location
  default_table_expiration_ms = 3600000
  delete_contents_on_destroy = true

}