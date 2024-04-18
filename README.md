# Pebble Webapp

## Overview
This repository contains the FastAPI code for the Pebble web application. The webapp can be accessed via DNS records set to:
- Documentation: http://pebble.fanp.co/docs
- API Documentation: http://pebble.fanp.co/redoc
- Example Endpoint: http://pebble.fanp.co/fibonacci/21 (Substitute other numbers for testing)

## Deployment
The main branch of this repository is what gets deployed. Additionally, a containerized version can be seen in the branch "containerized".

### Instructions
1. Connect to the jump box using the provided SSH key (`pebble-key.pem`). Ensure the key file permissions are set correctly:
<code>chmod 0400 pebble-key.pem</code>
<code>ssh -i pebble-key.pem admin@44.222.203.113</code>

2. To deploy the web application, use the following command on the jump box:
<code>make deploy</code>

### Redeployment
When new code is merged into the main branch, you can redeploy via the jump box using:
<code>make redeploy</code>
