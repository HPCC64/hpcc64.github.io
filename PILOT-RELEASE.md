# Release notes

Candidate only: content acceptance, Pages-source transition, merge and publication require separate owner authorization. Checks/reviews in PR #10 bind to its final SHA. **Do not merge while production depends on root `index.html`.**

## Authorized cutover sequence (not executed)

1. Record live Pages source, custom domain `lab.hpcc64.com`, HTTPS setting, deployed revision and a recoverable copy of the current root site. Recheck current main and candidate review. Existing DNS/redirects remain unchanged.
2. In a coordinated release window, switch Pages source from branch/root to **GitHub Actions before merging the root deletion**. Preserve the configured custom domain and HTTPS setting. [Actions publishing ignores CNAME files](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site); the retained root CNAME is historical/recovery material, not a domain-preservation mechanism for the new artifact. Allow for a publishing interruption; do not promise zero downtime.
3. Merge only the accepted candidate, confirm its resulting main tree, and record the full resulting main SHA. Manually dispatch `Publish Lab static site` on **main**, supplying that SHA as `expected_sha`. The workflow has no push/PR trigger, rejects a mismatched SHA before setup, and only permits main. These guards supplement owner authorization; they do not grant it.
4. The [Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) uploads only `./public` through `upload-pages-artifact`, then deploys it. README, AGENTS, release notes and root CNAME stay outside the artifact. Do not run it during candidate preparation.
5. Verify live page text/CSS, domain/TLS, cross-site links, mobile/keyboard, canonical/robots/sitemap, and a nested missing URL returning the styled 404. Keep the prior source/deployment until verification succeeds.

## Recovery

If switching settings fails before merge, retain the existing branch/root site and restore the recorded source settings under the release authorization. If failure occurs after merge, either redeploy a retained known-good Actions artifact or restore the prior root site (including CNAME) with a reviewed revert, **then** return Pages to the recorded branch/root source. Do not point branch publishing at a revision missing root index. Confirm restored content/domain; do not change DNS or delete history as a shortcut.

## Analytics and discovery

Cloudflare Web Analytics is [free](https://www.cloudflare.com/web-analytics/) and supports [sites outside its proxy](https://developers.cloudflare.com/web-analytics/get-started/). For GitHub Pages, the minimal later integration is the site's own dashboard-generated deferred beacon snippet before `</body>` on intended HTML pages. No dummy token, active snippet or analytics site registration is included. Activation needs separate approval; Google Analytics remains deferred.

Check existing account/zone injection first to avoid duplicate beacons or tracking other subdomains. [Free has zero custom rules; non-proxied tracking supports ten sites](https://developers.cloudflare.com/web-analytics/limits/). No plan upgrade or DNS/proxy change is needed. Source inspection cannot establish production tracking state.

After publication, use an already authorized Search Console ownership method and submit `https://lab.hpcc64.com/sitemap.xml`. No verification token or DNS change is included. Homepage canonical/Open Graph URLs agree; the 404 is noindex and absent from sitemap. Search indexing is not guaranteed.

Keep the shared black HPCC / red 64, white background and semantic expansion for future pub, with publication-appropriate reading layout. Exact local CSS values are not a new canonical identity. No shared runtime or extra site is introduced.

Read-only account check on 2026-11-02: hpcc64.com reports “Free Website”; the account Web Analytics site list is empty and the www Pages project has no analytics token configured. These are configuration observations, not a served-page measurement or authorization to activate tracking.
