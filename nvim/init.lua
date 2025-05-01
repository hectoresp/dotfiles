-- Añadir Lazy al runtime path
vim.opt.rtp:prepend(vim.fn.stdpath("config") .. "/lazy/lazy.nvim")

-- Plugin manager: Lazy
require("lazy").setup({
  -- LSP y autocompletado
  "neovim/nvim-lspconfig",
  "williamboman/mason.nvim",
  "williamboman/mason-lspconfig.nvim",
  "hrsh7th/nvim-cmp",
  "hrsh7th/cmp-nvim-lsp",
  "hrsh7th/cmp-buffer",
  "hrsh7th/cmp-path",
  "L3MON4D3/LuaSnip",
  "saadparwaiz1/cmp_luasnip",

  -- Syntax y árbol
  { "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },
  "nvim-tree/nvim-tree.lua",
  "nvim-tree/nvim-web-devicons",

  -- UI y estética
  "nvim-lualine/lualine.nvim",
  { "catppuccin/nvim", name = "catppuccin" },
  "lukas-reineke/indent-blankline.nvim",
  "lewis6991/gitsigns.nvim",

  -- Búsqueda
  "nvim-telescope/telescope.nvim",
  "nvim-lua/plenary.nvim",

  -- Otros
  "windwp/nvim-autopairs",
})

-- Tema
vim.cmd.colorscheme("catppuccin")

-- Línea de estado
require("lualine").setup()

-- Árbol de archivos
-- Configuración de Treesitter para Java
require('nvim-treesitter.configs').setup {
  ensure_installed = { "java" },  -- Asegura que Java esté instalado
  highlight = {
    enable = true,                 -- Habilita el coloreado
    additional_vim_regex_highlighting = false, -- Opcional
  },
}

-- Autopairs
require("nvim-autopairs").setup()

-- Gitsigns
require("gitsigns").setup()

-- Indent guides
require("ibl").setup()

-- Autocompletado
local cmp = require("cmp")
local luasnip = require("luasnip")
cmp.setup({
  snippet = {
    expand = function(args) luasnip.lsp_expand(args.body) end,
  },
  mapping = cmp.mapping.preset.insert({
    ["<Tab>"] = cmp.mapping.select_next_item(),
    ["<S-Tab>"] = cmp.mapping.select_prev_item(),
    ["<CR>"] = cmp.mapping.confirm({ select = true }),
  }),
  sources = cmp.config.sources({
    { name = "nvim_lsp" },
    { name = "luasnip" },
    { name = "buffer" },
    { name = "path" },
  }),
})

-- LSP setup
require("mason").setup()
require("mason-lspconfig").setup({
  ensure_installed = { "lua_ls", "pyright", "clangd" },
})

local lspconfig = require("lspconfig")
require("mason-lspconfig").setup_handlers({
  function(server_name)
    lspconfig[server_name].setup({
      capabilities = require("cmp_nvim_lsp").default_capabilities(),
    })
  end,
})

-- Configuración básica para NvimTree
require("nvim-tree").setup({
  update_cwd = true,  -- Cambiar el directorio de trabajo al abrir la carpeta
  view = {
    width = 30,  -- Ancho del árbol
    side = "left",  -- Mostrar el árbol a la izquierda
  },
})

