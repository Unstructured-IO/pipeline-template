# The sample-docs/ convention

Preprocessing pipeline API repositories may include sample documents (inputs) that could be posted to its API(s). By convention, this is the directory to place them in.

Naturally, adding a few small files directly in this directory with `git add` is fine. However, if the sample docs are larger files (or they are many smaller ones), it is recommended to provide a `make` target instead to download the files. E.g. [make dl-test-artifacts](https://github.com/Unstructured-IO/pipeline-sec-filings/blob/083b56f/Makefile#L136) in [pipeline-sec-filings](https://github.com/Unstructured-IO/pipeline-sec-filings/).

If your pipeline is not going to have sample-docs, go ahead and delete this README.md (and folder) :)
