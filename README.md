# Minghao Li | Publications

A public collection of Minghao Li's research papers, project documents, thesis material, and presentations, with direct browser-based access to every document.

This repository brings together written research and supporting presentations in one searchable library. It is designed to make the materials easy to browse, review, and share with researchers, collaborators, and readers interested in the underlying projects. Each document has a short, dedicated reading URL that can be included in a CV, portfolio, project page, or email.

The current collection contains **21 documents: 16 research papers and documents, and 5 presentations and reports**. Topics represented in the collection include machine learning for medical diagnosis, multimodal hateful-meme detection, 3D and 4D reconstruction, Gaussian representations, mathematical modeling, optimization, and economic and customer-data analysis. The library also includes project demonstrations and an internship report. Entries include different document types and stages of work; inclusion here does not imply peer-reviewed publication.

### Features

- **Direct online reading:** open a document in a full-page reader without navigating a repository file listing.
- **Short, shareable URLs:** use memorable paths such as `/peanut/`, `/nexus/`, and `/4d-rigging/`.
- **Searchable catalog:** find documents by title on the library homepage.
- **Preserved document titles:** short filenames keep URLs concise while the catalog retains descriptive titles.
- **Compatibility with earlier reader links:** previously shared long HTML addresses redirect to the new short pages.
- **Simple static hosting:** HTML, CSS, JavaScript, and PDF files are served through GitHub Pages, with no backend service or external CDN dependencies.

## Read Online

[Browse the Library](https://suleynanauir.github.io/minghao-li-publications/) · [GitHub Repository](https://github.com/SuleynanAuir/minghao-li-publications)

Each link opens a dedicated full-page PDF reader. Previously shared long reader URLs redirect to the corresponding short URL. Plain-text link list: [paper-links.txt](paper-links.txt).

### Research Papers and Documents

| No. | Document | Read Online |
| --- | --- | --- |
| 1 | A Unified Model for Intelligent Diagnosis-Synergizing Machine Learning and Reinforcement Learning | [ai-diagnosis](https://suleynanauir.github.io/minghao-li-publications/ai-diagnosis/) |
| 2 | A co-deployment strategy of decoy bombs based on geometric field of view masking and intelligent optimization | [decoy-strategy](https://suleynanauir.github.io/minghao-li-publications/decoy-strategy/) |
| 3 | Clinical Brain Tumor Detection- Optimized Machine Learning Frameworks for MRI Diagnosis | [brain-tumor](https://suleynanauir.github.io/minghao-li-publications/brain-tumor/) |
| 4 | Construction of Motion Simulation and Optimization Model of Bench Dragon Based on Spiral Path | [bench-dragon](https://suleynanauir.github.io/minghao-li-publications/bench-dragon/) |
| 5 | Echoes of Value- How Customer Patterns Predict Profits and What the Data Say Aloud | [customer-value](https://suleynanauir.github.io/minghao-li-publications/customer-value/) |
| 6 | Forecast and Analysis of Economic Development in the Guangdong-Hong Kong-Macao Greater Bay Area | [gba-economy](https://suleynanauir.github.io/minghao-li-publications/gba-economy/) |
| 7 | From Alignment to Reasoning in Detecting Hateful Memes | [hateful-memes](https://suleynanauir.github.io/minghao-li-publications/hateful-memes/) |
| 8 | HateReasoner | [hatereasoner](https://suleynanauir.github.io/minghao-li-publications/hatereasoner/) |
| 9 | Multi-level Chess Game Design | [chess](https://suleynanauir.github.io/minghao-li-publications/chess/) |
| 10 | NEXUS | [nexus](https://suleynanauir.github.io/minghao-li-publications/nexus/) |
| 11 | NEXUS Servy | [nexus-survey](https://suleynanauir.github.io/minghao-li-publications/nexus-survey/) |
| 12 | P-ADON4PDF | [p-adon](https://suleynanauir.github.io/minghao-li-publications/p-adon/) |
| 13 | PEANUT Prompt Enhanced Ablation | [peanut](https://suleynanauir.github.io/minghao-li-publications/peanut/) |
| 14 | Unified Automatic Rigging and 4D Gaussian Reconstruction | [4d-rigging](https://suleynanauir.github.io/minghao-li-publications/4d-rigging/) |
| 15 | Unified Automatic Rigging and 4D Gaussian Reconstruction in Robust Structure partial thesis | [4d-thesis](https://suleynanauir.github.io/minghao-li-publications/4d-thesis/) |
| 16 | Unveiling the Timeworn Scars and Knowledge of Stairs | [stairs](https://suleynanauir.github.io/minghao-li-publications/stairs/) |

### Presentations and Reports

| No. | Document | Read Online |
| --- | --- | --- |
| 17 | E Deformable Gaussians General | [deformable-gaussians](https://suleynanauir.github.io/minghao-li-publications/deformable-gaussians/) |
| 18 | FYP IncPoseFree meeting | [incposefree](https://suleynanauir.github.io/minghao-li-publications/incposefree/) |
| 19 | NEXUS demo | [nexus-demo](https://suleynanauir.github.io/minghao-li-publications/nexus-demo/) |
| 20 | Peanut demo | [peanut-demo](https://suleynanauir.github.io/minghao-li-publications/peanut-demo/) |
| 21 | internship report demo | [internship](https://suleynanauir.github.io/minghao-li-publications/internship/) |

## How the Library Works

The homepage lists the documents and provides title-based filtering. Each document opens on its own reading page, where an `iframe` fills the browser viewport and displays the PDF using the browser's built-in viewer. Page navigation, zoom, and in-document search depend on the capabilities of that viewer.

Visitors generally do not need to save a file manually or open a separate application. PDF data still needs to be transferred to the browser, and larger documents may take longer to load. Browser download preferences and some mobile browsers can prevent embedded viewing; each reader includes a fallback link to open the PDF directly. Full-page reading refers to filling the webpage viewport, rather than automatically activating the browser's fullscreen mode.

## Repository Structure

| Path | Purpose |
| --- | --- |
| `index.html` | Generated document catalog and entry point for the website. |
| `style.css` / `search.js` | Catalog styling and title search. |
| `publications.json` | Document metadata, short identifiers, PDF paths, categories, and legacy reader filenames. |
| `<id>/index.html` | Generated full-page reader, such as `peanut/index.html`. |
| `readers/` | Redirect pages for previously shared long reader URLs. |
| `additional-backup/` | Research PDFs and locally retained originals. |
| `additional-backup/demo/` | Presentation PDFs and locally retained originals. |
| `output/pdf/` | Optimized web copies used for selected larger documents. |
| `scripts/build.py` | Standard-library Python generator for the catalog, readers, redirects, and link lists. |
| `paper-links.txt` | Document titles and complete reading URLs in a copyable plain-text format. |
| `.nojekyll` | Keeps the site suitable for direct static-file publication. |

## Update the Collection

1. Add a PDF with a concise filename to `additional-backup/` or its `demo/` subdirectory.
2. Add or update its entry in `publications.json` using the fields below.
3. If the document has an optimized web copy, update that copy as well.
4. Run the generator from the repository root:

   ```sh
   python3 scripts/build.py
   ```

5. Review and commit the PDF, metadata, generated pages, README link tables, and `paper-links.txt`.

| Field | Meaning |
| --- | --- |
| `id` | Unique URL-safe identifier, such as `peanut`; determines the reading URL. |
| `title` | Full display title shown in the catalog and link lists. |
| `pdf` | PDF path relative to the repository root. |
| `legacy` | Filename of the compatibility page under `readers/`; use a unique filename for each entry. |
| `category` | `research` for research documents or `demo` for presentations and reports. |

Keep an existing `id` unchanged to preserve its short reading URL. The generator prefers a matching file under `output/pdf/` when one exists, so replacing only the local original will not update the published web copy. Removing a metadata entry does not automatically delete previously generated pages; remove obsolete pages explicitly when retiring a document.

The generator updates the **Read Online** section of this README and the plain-text link list in English. The introductory and maintenance sections are maintained separately. Legacy compatibility applies to the old HTML reader URLs; direct PDF URLs change when the corresponding PDF is renamed.

## Optimized PDF Copies

Selected large documents use smaller web copies to improve loading times. Their original files are retained locally and excluded from Git through `.gitignore`; those originals are not included in a fresh clone.

| Web copy | Image resolution used for optimization |
| --- | --- |
| `output/pdf/peanut.pdf` | 180 dpi |
| `output/pdf/demo/nexus-demo.pdf` | 120 dpi |
| `output/pdf/demo/peanut-demo.pdf` | 180 dpi |
| `output/pdf/demo/internship.pdf` | 180 dpi |

Optimization reduces image resolution while retaining the document's pages and text. The remaining documents are served from `additional-backup/`. Maintain both the original and its web copy when updating an optimized document.

## GitHub Pages Deployment

The live library is hosted at [suleynanauir.github.io/minghao-li-publications](https://suleynanauir.github.io/minghao-li-publications/).

The repository publishes the root directory of the `main` branch through GitHub Pages. Generated HTML files and the PDFs they reference must be committed; the Python generator is run locally before publication. No Node.js installation, package manager, or application server is required.

To configure an equivalent deployment, open **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, and select **main** with **/(root)**. See the [GitHub Pages publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) for configuration details.

For a local preview, serve the repository root:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000/` in a browser. Relative document paths support both local previews and the GitHub Pages project URL.

## Sharing and Referencing

Use the dedicated short reader URL when sharing a document. A complete list is available in [paper-links.txt](paper-links.txt), and the catalog above provides clickable links for every entry. For academic references, use the authors, title, date, and publication information stated in the individual document rather than inferring publication details from its repository filename.
