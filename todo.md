# Vodafone Ziggo Voice Assistant Build Checklist

## Phase 1: Git Setup & Repository Seeding
- [x] Git-initialize the local directory `voda-ziggo-voice` and link it to the empty GitHub repository `git@github.com:horseback-jp/vz-voice-build.git`
- [x] Pull the live GECX conversational agent state (`c118ecd7-854e-4918-b680-6b9aaad29358`) from Google Cloud into `cxas_app/` to seed our baseline configuration files
- [x] Clone the generalized synchronizer repository `git@github.com:horseback-jp/agent-repo-sync.git`, copy `prune_gecx_assets.py`, and tailor it specifically for the Vodafone Ziggo agent variables

## Phase 2: PRD Deep-Dive & Architecture Design
- [x] Parse and read the Product Requirements Document (PRD) `VZ - Product Requirements Document (PRD).pdf` using GECX specs
- [x] Design the GECX voice assistant architecture: Global instructions, specialist sub-agents, variables, and API tool schemes

## Phase 3: GitOps Pipeline & Deployment Setup
- [x] Extract the successful Lloyds Bank `.github/workflows/deploy.yaml` template and transplant it into the Vodafone Ziggo repo to establish automated GitHub Action GitOps deployments
- [x] Refactor all GECX orchestrator JSON, tools python code, and global instructions according to the PRD
- [x] Run local GECX linter (`cxas lint`) inside the workspace to guarantee 100% structural compilation status

## Phase 4: Push & Live Synchronization Verification
- [ ] Stage, commit, and push the code to GitHub to trigger the automated deployment pipeline
- [ ] Execute `prune_gecx_assets.py` to verify that your local repository and the GECX live agent are 100% cleanly in sync
