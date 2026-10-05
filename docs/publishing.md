# Publish this folder on GitHub

**Extract the ZIP first.** Upload the extracted repository files so that `README.md` is at the repository root. Uploading the ZIP as one file only stores the archive; it does not populate the repository with its contents.

Suggested repository name: **`awesome-foundation-model-lifecycle`**

Suggested description:

> Papers, benchmarks, and resources on foundation model robustness across pretraining, adaptation, deployment, and feedback. Companion to Robustness in Foundation Models.

Suggested GitHub topics: `awesome-list`, `foundation-models`, `robustness`, `self-supervised-learning`, `multimodal-learning`, `model-editing`, `uncertainty-quantification`, `explainable-ai`, `red-teaming`, `continual-learning`.

## Option A: GitHub Desktop

Create a local repository from the extracted folder, commit its contents, then use GitHub Desktop to publish it under your account. This route also preserves the included `.github` directory containing validation and contribution templates.

## Option B: Git

Create an empty GitHub repository under your account. Do not initialize it with a second README or license. In a terminal opened inside the extracted folder, replace `YOUR_GITHUB_USERNAME` with your actual account:

```bash
git init
git branch -M main
git add .
git commit -m "Add lifecycle-centered foundation model robustness collection"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/awesome-foundation-model-lifecycle.git
git push -u origin main
```

Use your normal GitHub authentication. The ZIP contains no Git history, credentials, tokens or remote configuration.

## Option C: Browser upload

Create a repository, open **Add file → Upload files**, and upload the extracted contents. Ensure folders retain their structure and `README.md` appears at the root. Your file picker may hide dot-prefixed items; include `.github`, `.gitignore` and `.gitattributes` using your system's show-hidden-files option, or use Git/GitHub Desktop for the complete folder.

GitHub's [file-upload documentation](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) describes the browser and command-line routes. This package is small enough for ordinary upload.

## Check the published view

Open the README, follow a reading-path link, expand/render the lifecycle Mermaid diagram, and check the Actions tab for the validation workflow. Fill the short author-supplied checklist in [maintainer notes](maintainer-notes.md). Add the repository description and topics in the GitHub About panel.

If a workflow is absent after browser upload, verify that `.github/workflows/validate.yml` was included. Figures remain optional; the initial README uses explicit TODO text rather than broken image links.
