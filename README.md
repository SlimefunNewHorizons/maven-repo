<!-- credits:start -->
> **Credits & license.** Port and maintenance by [JackStar6677-1](https://github.com/JackStar6677-1) and [DrakesCraft Labs](https://github.com/SlimefunNewHorizons). Original authors: [jack](https://github.com/jack), [JackStar6677](https://github.com/JackStar6677). Upstream license: **GNU General Public License v3.0** (see [LICENSE](LICENSE)). Details: [docs/UPSTREAM_ATTRIBUTION.md](docs/UPSTREAM_ATTRIBUTION.md) · Policy: [Rights & Attribution](https://github.com/SlimefunNewHorizons/.github/blob/main/RIGHTS_AND_ATTRIBUTION.md). Independent community project, not affiliated with or endorsed by the original authors or the official Slimefun team.
>
> **Créditos y licencia.** Port y mantenimiento por [JackStar6677-1](https://github.com/JackStar6677-1) y [DrakesCraft Labs](https://github.com/SlimefunNewHorizons). Autores originales: [jack](https://github.com/jack), [JackStar6677](https://github.com/JackStar6677). Licencia original: **GNU General Public License v3.0**. Detalle en [docs/UPSTREAM_ATTRIBUTION.md](docs/UPSTREAM_ATTRIBUTION.md).
<!-- credits:end -->

<div align="center">

  <img src="https://raw.githubusercontent.com/SlimefunNewHorizons/maven-repo/main/banner.svg" alt="DrakesCraft Labs Maven Repository" width="920" />

# DrakesCraft Labs Maven Repository

**Shared Maven & Gradle artifact repository for the Slimefun: New Horizons & DrakesCraft Labs ecosystem**

[![Live Portal](https://img.shields.io/badge/Portal-maven.drakescraft.cl-0EA5E9?style=for-the-badge)](https://maven.drakescraft.cl)
[![Production](https://img.shields.io/badge/Production-MC_1.21.11_%C2%B7_Java_21-22C55E?style=for-the-badge&logo=openjdk&logoColor=white)](https://maven.drakescraft.cl/#lineas)
[![Season 2](https://img.shields.io/badge/T2-MC_26.2_%C2%B7_Java_25-6366F1?style=for-the-badge&logo=openjdk&logoColor=white)](https://maven.drakescraft.cl/#lineas)
[![GitHub Pages](https://img.shields.io/badge/Hosted_on-GitHub_Pages-181717?style=for-the-badge&logo=github)](https://github.com/SlimefunNewHorizons/maven-repo)

[Web Portal](https://maven.drakescraft.cl) ·
[Compatibility Matrix](./docs/COMPATIBILITY.md) ·
[Manifest JSON](https://maven.drakescraft.cl/manifest.json) ·
[DrakesCraft Network](https://web.drakescraft.cl) ·
[Discord](https://discord.gg/rv3vtXZTk7)

</div>

---

## Overview

`https://maven.drakescraft.cl` publishes the shared Maven artifacts of the **Slimefun: New Horizons / DrakesCraft Labs** ecosystem so standalone plugins and suites compile reproducibly in CI/CD without local reactor builds or manually installed JARs.

## Version Lines

> **Important:** The `1.21.11` (Java 21) and `26.x` (Java 25) lines are **not binary-interchangeable**. Package namespaces, Paper/Purpur APIs, and target JDK versions differ; always compile against the matching line.

| Line | Minecraft | Java | Slimefun Package | Dough Package | Core Artifacts |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **Production** | `1.21.11` | `21` | `com.github.drakescraft_labs.slimefun4` | `dev.drake.dough` | `slimefun-core:11.0-Drake-1.21.11-SNAPSHOT`, `dough-core:1.3.1-DRAKE-v11-SNAPSHOT`, `SefiLib:0.3.0-Drake-1.21.11` |
| **Season 2 (T2)** | `26.2` | `25` | `io.github.thebusybiscuit.slimefun4` | `io.github.bakedlibs.dough` | `slimefun-core:11.0-Universal-26.x-SNAPSHOT`, `dough-core:1.3.1-Universal-26.x-SNAPSHOT`, `SefiLib:0.3.1-Universal-26.x-SNAPSHOT` |

See [`docs/COMPATIBILITY.md`](./docs/COMPATIBILITY.md) for the full compatibility matrix.

## Maven Configuration

```xml
<repositories>
  <repository>
    <id>drakescraft-labs</id>
    <url>https://maven.drakescraft.cl</url>
  </repository>
</repositories>
```

## Gradle (Kotlin DSL) Configuration

```kotlin
repositories {
    maven("https://maven.drakescraft.cl")
}
```

## License

Artifact licenses follow their respective upstream open-source projects. Repository tooling and portal assets are licensed under [`LICENSE`](./LICENSE).
