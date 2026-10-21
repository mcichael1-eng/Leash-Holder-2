-- Pandoc filter for the AI Field Guide.
-- 1. Mermaid code blocks become <pre class="mermaid-src"> for build.py to render.
-- 2. Labelled blockquotes become callout divs (definition, key idea, analogy, ...).

local kinds = {
  ["Key idea"] = "key",
  ["Analogy"] = "analogy",
  ["Try it"] = "try",
  ["Watch out"] = "watch",
}

local used_ids = {}

local function slug(s)
  s = s:lower():gsub("[^%w%s%-]", ""):gsub("%s+", "-"):gsub("%-+", "-")
  return s
end

local function unique(id)
  if not used_ids[id] then used_ids[id] = 1 return id end
  used_ids[id] = used_ids[id] + 1
  return id .. "-" .. used_ids[id]
end

function CodeBlock(el)
  if el.classes:includes("mermaid") then
    local esc = el.text:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;")
    return pandoc.RawBlock("html", '<pre class="mermaid-src">' .. esc .. "</pre>")
  end
end

function BlockQuote(el)
  local first = el.content[1]
  if not first or (first.t ~= "Para" and first.t ~= "Plain") then return nil end
  local lead = first.content[1]
  if not lead or lead.t ~= "Strong" then return nil end
  local label = pandoc.utils.stringify(lead)
  -- Definition — Term:
  local term = label:match("^Definition%s*[—%-]+%s*(.-):?%s*$")
  if term and term ~= "" then
    term = term:gsub(":$", "")
    first.content[1] = pandoc.Span(pandoc.Inlines(term), {class = "def-term"})
    local div = pandoc.Div(el.content, {class = "callout def"})
    div.identifier = unique("def-" .. slug(term))
    div.attributes["data-term"] = term
    return div
  end
  if label:match("^At the frontier") then
    local clean = label:gsub(":%s*$", "")
    first.content[1] = pandoc.Span(pandoc.Inlines(clean), {class = "callout-label"})
    return pandoc.Div(el.content, {class = "callout frontier"})
  end
  for name, cls in pairs(kinds) do
    if label:match("^" .. name:gsub("%s", "%%s") .. ":?%s*$") then
      first.content[1] = pandoc.Span(pandoc.Inlines(name), {class = "callout-label"})
      return pandoc.Div(el.content, {class = "callout " .. cls})
    end
  end
  return nil
end
