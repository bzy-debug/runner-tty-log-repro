# Gitea/GitHub CI log TTY repro

This repository is a minimal reproduction for gitea/runner issue 956:

<https://gitea.com/gitea/runner/issues/956>

It keeps equivalent workflow content in both CI locations:

- `.gitea/workflows/tty-log-repro.yml` for Gitea Actions on `ubuntu-latest`
- `.gitea/workflows/tty-log-repro-host.yml` for manual Gitea host-runner reproduction
- `.github/workflows/tty-log-repro.yml` for GitHub Actions

The workflow prints whether stdout is a TTY, then runs a tiny Python progress
renderer that behaves like tools such as Docker Build with `--progress=auto`:

- TTY stdout: emit carriage-return redraw frames.
- Non-TTY stdout: emit plain line-oriented output.

Expected result:

- GitHub Actions hosted Ubuntu and macOS runners: `shell_stdout_is_tty=false` and `python_stdout_isatty=false`.
- Gitea Actions `ubuntu-latest` runner: compare its log against GitHub's hosted Ubuntu log.
- Gitea runner host mode: `shell_stdout_is_tty=true`, `python_stdout_isatty=true`, and Docker Build terminal-redraw output is preserved in the job log.

The Gitea host workflow is manual-dispatch-only and uses the placeholder label
`internal-host-runner` by default. A private Gitea instance can dispatch that
workflow with the real host-runner label without committing the internal runner
name to the public repository.

The optional Docker step runs `docker build --progress=auto` when Docker is
available, matching the real-world behavior described in the issue.
