import json

template = '''
{
    // Rough modified version of Celeste to darken it up
    "name": "Celeste Dark",
    "author": "Sublime HQ Pty Ltd",
    "variables":
    {
        // These colors are part of the hashed range
        // and should only be used in non-source
        "purple": "#A68CD9",
        "blue": "#3CA7DD",
        "teal": "#3CDDC2",
        "green": "#3CDD57",
        // End of hashed range colors
        "red": "#F4BEBE",
        "orange": "#F7A76E",
        "dark_orange": "#F7856E",
        "yellow": "#FFE666",
        "brown": "#D2BFAC",
        "light_brown": "#E4D9CD",
        "dark_brown": "#634D36",
        "magenta": "#FF80B5",
        "light_gray": "#f6f6f6",
        "dark_gray": "#202020",
        "black": "#000000",
        "whitesmoke": "#FFFFFF)",
        "gray": "#909090",
        "ccc":"#c0c0c0",
        "lelele": "#1e1e1e",
        "sevens": "#707070",
        "twenties": "#202020",
        "threes": "#303030",
        "bees": "#b0b0b0"
    },
    "globals":
    {
        "foreground": "var(whitesmoke)",
        "background": "var(black)",
        "caret": "var(magenta)",
        "selection": "color(var(light_gray) a(0.08))",
        "selection_border": "color(var(light_gray) a(0.3))",
        "inactive_selection": "color(var(light_gray) a(0.06))",
        "line_highlight": "var(threes)",
        "highlight": "var(magenta)",
        "find_highlight": "var(yellow)",
        "find_highlight_foreground": "var(dark_brown)",
        "active_guide": "var(red)",
        "stack_guide": "var(orange)",
        "shadow": "var(bees)",
        "accent": "var(orange)",
        "misspelling": "var(dark_orange)",
        "fold_marker": "var(yellow)"
    },
    "rules":
    [
        {
            "scope": "text",
            "foreground": "var(ccc)"
        },
        {
            "scope": "source - comment - string - keyword - punctuation - storage - entity - source.css",
            "foreground": ["var(green)", "var(purple)"]
        },
        {
            "scope": "comment",
            "foreground": "var(gray",
            "font_style": "italic"
        },
        {
            "scope": "entity.name - entity.name.tag - entity.name.section",
            "foreground": "var(orange)",
            "background": "var(lelele)"
        },
        {
            "scope": "entity.other.inherited-class",
            "foreground": "var(dark_orange)",
            "background": "var(lelele)"
        },
        {
            "scope": "support.function.builtin, support.class.builtin, variable.language",
            "foreground": "var(whitesmoke)",
            "font_style": "italic"
        },
        {
            "scope": "keyword.operator",
            "foreground": "var(sevens)"
        },
        {
            "scope": "keyword, constant.language",
            "foreground": "var(whitesmoke)",
            "font_style": "italic"
        },
        {
            "scope": "constant.numeric",
            "foreground": "var(red)"
        },
        {
            "scope": "constant.character",
            "foreground": "var(dark_orange)"
        },
        {
            "scope": "storage, support.type.sys-types",
            "foreground": "var(whitesmoke)",
            "font_style": "italic"
        },
        {
            "scope": "string",
            "foreground": "var(brown)"
        },
        {
            "scope": "punctuation.definition.string",
            "foreground": "var(light_brown)"
        },
        {
            "scope": "punctuation",
            "foreground": "var(sevens)"
        },
        {
            "scope": "meta.function-call variable.parameter",
            "foreground": "var(light_brown)"
        },
        {
            "scope": "invalid.illegal",
            "background": "var(red)"
        },
        {
            "scope": "invalid.deprecated",
            "background": "var(red)"
        },
        // HTML
        {
            "scope": "entity.name.tag",
            "foreground": "var(blue)"
        },
        // HTML/CSS
        {
            "scope": "entity.other.attribute-name",
            "foreground": "var(teal)"
        },
        {
            "scope": "entity.other.attribute-name.id",
            "foreground": "var(orange)"
        },
        // CSS
        {
            "scope": "support.type.property-name",
            "foreground": "var(purple)"
        },
        {
            "scope": "support.type.vendor-prefix",
            "foreground": "var(blue)"
        },
        {
            "scope": "entity.other.pseudo-class",
            "foreground": "var(green)"
        },
        // Markdown
        {
            "scope": "markup.heading.1 entity.name.section",
            "foreground": "var(blue)",
            "font_style": "bold"
        },
        {
            "scope": "markup.heading.2 entity.name.section",
            "foreground": "var(blue)"
        },
        {
            "scope": "entity.name.section",
            "foreground": "var(teal)"
        },
        {
            "scope": "markup.italic",
            "foreground": "var(black)",
            "font_style": "italic"
        },
        {
            "scope": "markup.bold",
            "foreground": "var(black)",
            "font_style": "bold"
        },
        {
            "scope": "markup.list punctuation.definition.list_item",
            "foreground": "var(dark_orange)"
        },
        {
            "scope": "markup.raw",
            "background": "var(twenties)"
        },
        {
            "scope": "markup.raw constant.other.language-name",
            "foreground": "var(green)",
            "font_style": "italic"
        },
        {
            "scope": "meta.table.header - punctuation",
            "font_style": "bold"
        }
    ]
}
'''



col = json.load(open('/home/sheffler/.cache/wal/colors.json'))
col = {**col['special'], **col['colors']}
print(col)
