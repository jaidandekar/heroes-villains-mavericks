# Development and release notes

Work on a `codex/` development branch. Codex and Cursor can use the same checkout. Keep the current site in `site/` as the compatibility baseline while prototyping the new build outside that directory. The Pages artifact builds `editorial-preview/` and overlays it on the retained `site/` routes.

## Compatibility baseline

- [Legacy routes](../tools/legacy_routes.json) records the 34 existing HTML outputs, including both homepage paths and all 32 guides. Preserve the public project base path and existing external links when testing the new build.
- Keep `#run/<slug>` reading links and guide section anchors working; account for `#version/<slug>` and `#all-versions`, which currently lead to the variants section. Route and static link checks do not exercise fragments handled by JavaScript.
- The guide generator is the source for committed guide HTML. Change the template, packs, or art maps and regenerate, then inspect the diff. Do not use the screen refresh to make cosmetic homepage changes: it rebuilds the entire page from its own template and curated slate.
- Capture browser baselines before migrating design: desktop and mobile homepage, carousel and keyboard navigation, a complex mantle guide (Green Lantern), a focused character guide (Miles Morales), and a team guide (Fantastic Four). Include long copy, missing art, and reduced motion. The offline checks are separate from that future browser suite.

## Production release

1. Verify the release-gated deployment workflow is already in `main` before treating pushes as safe. The old workflow on `main` remains in effect until the workflow change lands. Check the actual Pages source and `github-pages` environment settings in GitHub.
2. Publishing runs only when `editorial-preview/release-request.txt` changes on `main`, or when the workflow is manually dispatched. Ordinary development pushes do not deploy. Update the release request only after explicit owner approval. Review the site and validation results. Obtain explicit owner approval for the exact `main` revision before dispatching **Deploy site to GitHub Pages**. The workflow accepts dispatches from `main` only and runs offline checks before uploading the artifact.
3. Record the approved revision and Actions run. Verify both public homepage URLs used by the site and representative guide and reading links after deployment.
4. To roll back, prepare a reviewed revert on `main` that restores the previous known-good site files while retaining the manual deployment controls. Validate and obtain approval for that revision, then update `editorial-preview/release-request.txt` in that approved revision or dispatch the same workflow. Do not reset branch history.
