variable "credentials" {
  description = "accounts credentials"
  default = "./Keys/google-cloud-cred.json"
}

variable "service_location" {
  description = "define location for all the services"
  default = "EU"
}

variable "service_region" {
  description = "default region for provider"
  default =  "europe-west2"
  
}

