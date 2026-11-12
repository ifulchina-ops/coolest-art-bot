# Coolest Art — make.fun `coolest-art-01`

Entry for the make.fun "Make the coolest art" bounty ($250, top 20 share).

## The art

**"Neon Horizon"** — a lone astronaut in silhouette stands on a glowing
neon ridge of an alien world, gazing up at a huge ringed planet filling a
violet-and-teal sky. Bold silhouette, strong diagonal composition, and vivid
cyan/magenta light against deep shadow, built to read clearly even at
thumbnail size (~300 px), which is one of the judge's stated criteria.

The image (`art.png`) is 1024×1024, 453,735 bytes — inside the 1 MiB /
1024×1024 gate. It was generated with an image model and then resized and
palette-optimised (PIL, 256-colour adaptive palette, Floyd–Steinberg
dithering) to fit the size limit without changing the subject.

## How it runs

`main.py` (Python 3.13, stdlib only) copies `art.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to `/output/entry.png`. A pure
byte copy, so two runs always write identical bytes.

Local check:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# -> out/entry.png, byte-identical to art.png
```

## Files

- `main.py` — the entry program
- `art.png` — the artwork
- `LICENSE` — MIT
