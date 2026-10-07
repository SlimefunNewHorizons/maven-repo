# Publicacion De Artefactos Drake

Este repo es la base publica de dependencias para los plugins de DrakesCraft Labs. La regla practica:

1. Compila el plugin o libreria en su repo fuente.
2. Publica el jar aqui con `scripts/Publish-DrakeArtifact.ps1` o con el manifest `catalog/drake-artifacts.json`.
3. Haz commit y push de los archivos generados en este repo.
4. En el plugin consumidor, apunta a `https://maven.drakescraft.cl/`.
5. Valida con una cache Maven/Gradle temporal limpia.

## Publicar Un Artefacto

```powershell
.\scripts\Publish-DrakeArtifact.ps1 `
  -ArtifactFile "..\standalone-audit\NetworksV6-drake\target\NetworksV6-Drake-v11-SNAPSHOT.jar" `
  -ArtifactId "NetworksV6-drake" `
  -Version "11-SNAPSHOT" `
  -Description "Jar compilado de NetworksV6 Drake"
```

El script genera un POM minimo independiente, publica el jar en formato Maven y recalcula checksums.

## Publicar Desde Manifest

```powershell
.\scripts\Publish-DrakeManifest.ps1 -ManifestPath .\catalog\drake-artifacts.json
```

El manifest es la lista controlada de artefactos Drake que queremos exponer como base descargable. Se puede ir ampliando con los plugins del monorepo y los repos independientes.

## Politica

- Publica aqui solo artefactos que otros plugins necesiten o que queramos distribuir como base Drake controlada.
- Evita POMs que dependan de parents locales del reactor.
- Prefiere versiones con sufijo Drake cuando el codigo fue modificado por la organizacion.
- No publiques secretos, configs de servidor ni archivos de runtime.

## Coordenadas Universales 26.x

Linea separada de la 1.21.11 (versiones distintas para no pisar `~/.m2`):

| Artefacto | Version | Origen | Bytecode |
|---|---|---|---|
| `slimefun-core` | `11.0-Universal-26.x-SNAPSHOT` | `Slimefun4-Drake` rama `fix/ticket-75-universal` (incluye `feat/universal-slimefun-abi`) | Java 21 |
| `infinitylib-drake` | `1.3.11-UNIVERSAL-26x-SNAPSHOT` | `DrakeInfinityLib` rama `port-26x` | Java 25 |

El core universal expone los paquetes upstream `io.github.thebusybiscuit.slimefun4.*`; los addons port-26x deben compilar contra estas coordenadas y no contra `11.0-Drake-1.21.11-SNAPSHOT`. Ambos se publican con POM minimo (sin parent del reactor): declara `slimefun-core` como `provided` en el addon consumidor.
