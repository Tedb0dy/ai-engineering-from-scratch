# My progress notes
- [x] Phase 0 / 01 Dev environment
- [x] Phase 0 / 02 Git & collaboration
- [x] Phase 0 / 03 GPU setup & cloud
  - 5000x5000 matmul (250 GFLOP): ThinkPad 0.75s (~333 GFLOPS) | Colab T4 fp32 0.088s (~2.8 TFLOPS)
  - T4 = 15 GB VRAM -> ~7.5B params fp16 weights only; ~1B to train with Adam
