# Pebble Webapp

## Overview
This repository contains the FastAPI code for the Pebble web application. The webapp can be accessed via DNS records set to:
- Documentation: http://pebble.fanp.co/docs
- API Documentation: http://pebble.fanp.co/redoc
- Example Endpoint: http://pebble.fanp.co/fibonacci/21 (Substitute other numbers for testing)

## Deployment
View the Ansible code and supporting files at: https://github.com/fampton/pebbleinfra

### Redeployment
When new code is merged into the main branch, you can redeploy via the jump box using:
<code>make redeploy</code>
