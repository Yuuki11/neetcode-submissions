class TextProcessor:
    def format_text(self, a: str, b: str = None) -> str:
        if b is None:
            return a.upper()
        return a + b

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
