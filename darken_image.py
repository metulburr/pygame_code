dark = pygame.Surface((image.get_width(), image.get_height()), flags=pygame.SRCALPHA)
dark.fill((50, 50, 50, 0))
image.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
#will subtract 50 from the RGB values of the surface called image.
