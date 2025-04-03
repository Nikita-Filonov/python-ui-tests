from elements.base_element import BaseElement


class Link(BaseElement):
    @property
    def type_of(self) -> str:
        return "link"
