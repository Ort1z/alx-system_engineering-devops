# Web Stack Debugging

## Overview

This repository contains configurations and scripts to debug and optimize a web stack. The goal is to ensure that the Nginx server can handle high concurrency without failing.

## Puppet Script

The `0-the_sky_is_the_limit_not.pp` Puppet script adjusts Nginx settings to handle 1000 requests with 100 concurrent requests efficiently. The script includes:

- Configuration for Nginx to handle high concurrency
- Notifications to restart the Nginx service when configurations are updated

## Usage

### Step 3: Validate and Test

1. **Apply the Puppet Manifest**:
   - Apply the Puppet manifest to ensure it makes the necessary changes to the Nginx configuration.

   ```bash
   puppet apply 0-the_sky_is_the_limit_not.pp
