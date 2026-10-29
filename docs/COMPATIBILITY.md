# Compatibility matrix

This repository hosts **two binary-incompatible lines** of the same libraries. Pick one line per server/addon and do not mix them.

| Artifact (`com.github.drakescraft_labs`) | Version | Minecraft | Java | Java package | dough package | Source branch |
|---|---|---|---|---|---|---|
| `slimefun-core` | `11.0-Drake-1.21.11-SNAPSHOT` | 1.21.11 | 21 | `com.github.drakescraft_labs.slimefun4` | `dev.drake.dough` | `main` of Slimefun4-Drake |
| `slimefun-core` | `11.0-Universal-26.x-SNAPSHOT` | 26.2 | 25 | `io.github.thebusybiscuit.slimefun4` | `io.github.bakedlibs.dough` | `port-26x` of Slimefun4-Drake |
| `dough-core` | `1.3.1-DRAKE-v11-SNAPSHOT` | 1.21.11 | 21 | n/a | `dev.drake.dough` | `main` of dough-core |
| `dough-core` | `1.3.1-Universal-26.x-SNAPSHOT` | 26.2 | 25 | n/a | `io.github.bakedlibs.dough` | `port-26x` of dough-core |
| `SefiLib` | `0.3.0-Drake-1.21.11` | 1.21.11 | 21 | `dev.sefiraat.sefilib` | n/a | `main` of SefiLib |
| `sefilib-drake` | `0.3.1-DRAKE-SNAPSHOT` | 1.21.11 | 21 | `dev.drake.sefilib` | n/a | legacy line (1.21.11) |
| `SefiLib` | `0.3.1-Universal-26.x-SNAPSHOT` | 26.2 | 25 | `dev.sefiraat.sefilib` | n/a | `port-26x` of SefiLib |

Also present for older servers: `slimefun-core 11.0-Drake-1.21.1-SNAPSHOT` (Minecraft 1.21.1).

**Warning: the 1.21.11 and 26.x lines are NOT binary-interchangeable.** Package names, Minecraft/Paper APIs and the required Java release differ. An addon compiled against one line will not load against the other; recompile it against the matching line. Naming rule: `-Drake-1.21.11` / `-DRAKE-*` = production line, `-Universal-26.x` = 26.2 line.

Note: `SefiLib 0.3.1-Universal-26.x` keeps the upstream `dev.sefiraat.sefilib` package, whereas the older `sefilib-drake` artifact relocated it to `dev.drake.sefilib`.

## Maven examples

```xml
<repositories>
  <repository>
    <id>drakescraft-labs</id>
    <url>https://maven.drakescraft.cl/</url>
    <snapshots><enabled>true</enabled></snapshots>
  </repository>
</repositories>
```

### Line 1.21.11 (Java 21)

```xml
<dependency>
  <groupId>com.github.drakescraft_labs</groupId>
  <artifactId>slimefun-core</artifactId>
  <version>11.0-Drake-1.21.11-SNAPSHOT</version>
  <scope>provided</scope>
</dependency>
<dependency>
  <groupId>com.github.drakescraft_labs</groupId>
  <artifactId>dough-core</artifactId>
  <version>1.3.1-DRAKE-v11-SNAPSHOT</version>
</dependency>
<dependency>
  <groupId>com.github.drakescraft_labs</groupId>
  <artifactId>SefiLib</artifactId>
  <version>0.3.0-Drake-1.21.11</version>
</dependency>
```

### Line 26.2 (Java 25)

```xml
<dependency>
  <groupId>com.github.drakescraft_labs</groupId>
  <artifactId>slimefun-core</artifactId>
  <version>11.0-Universal-26.x-SNAPSHOT</version>
  <scope>provided</scope>
</dependency>
<dependency>
  <groupId>com.github.drakescraft_labs</groupId>
  <artifactId>dough-core</artifactId>
  <version>1.3.1-Universal-26.x-SNAPSHOT</version>
</dependency>
<dependency>
  <groupId>com.github.drakescraft_labs</groupId>
  <artifactId>SefiLib</artifactId>
  <version>0.3.1-Universal-26.x-SNAPSHOT</version>
</dependency>
```

Snapshot hygiene: only the latest timestamped build of each snapshot version is kept in this repository.
