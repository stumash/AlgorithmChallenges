from typing import Iterator, Literal, Optional, Union

# The Grammar
#
# expression =
# | term
# | term ('+' | '-') term
#
# term =
# | factor
# | factor ('*' | '/') factor
#
# factor =
# | number
# | '(' expression ')'

# Lexer

TokenType = Union[
    Literal['LParen'], Literal['RParen'],
    Literal['Plus'], Literal['Minus'],
    Literal['Mult'], Literal['Div'],
    Literal['Number'],
]
class Token:
    def __init__(self, tp: TokenType, val: Optional[int] = None):
        self.tp = tp
        self.val = val
    def __repr__(self) -> str:
        if self.tp == 'Number': return f'{self.val}'
        elif self.tp == 'Plus': return 'Plus'
        elif self.tp == 'Minus': return 'Minus'
        elif self.tp == 'Mult': return 'Mult'
        elif self.tp == 'Div': return 'Div'
        elif self.tp == 'LParen': return 'LParen'
        elif self.tp == 'RParen': return 'RParen'
        raise Exception(f'invalid token type {self.tp}')

class Lexer:
    def __init__(self, s: str):
        self.s = s
    def tokens(self) -> Iterator[Token]:
        s = self.s
        i = 0
        while i < len(s):
            if s[i] in '1234567890':
                n_str = ''
                while i < len(s) and s[i] in '1234567890':
                    n_str += s[i]
                    i += 1
                yield Token('Number', int(n_str))
            else:
                if s[i] == '+': yield Token('Plus')
                if s[i] == '-': yield Token('Minus')
                if s[i] == '*': yield Token('Mult')
                if s[i] == '/': yield Token('Div')
                if s[i] == '(': yield Token('LParen')
                if s[i] == ')': yield Token('RParen')
                i += 1

# Parser

NodeType = Union[
    Literal['Plus'], Literal['Minus'],
    Literal['Mult'], Literal['Div'],
    Literal['Paren'], Literal['Number'],
]
class ASTNode:
    def __init__(self, tp: NodeType):
        self.tp = tp
    def calc(self) -> int:
        raise Exception('unimplented')
    def __repr__(self) -> str:
        raise Exception('unimplented')
class PlusNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        super().__init__('Plus')
        self.left, self.right = left, right
    def calc(self) -> int:
        return self.left.calc() + self.right.calc()
    def __repr__(self) -> str:
        return f'({self.left} + {self.right})'
class MinusNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        super().__init__('Minus')
        self.left, self.right = left, right
    def calc(self) -> int:
        return self.left.calc() - self.right.calc()
    def __repr__(self) -> str:
        return f'({self.left} - {self.right})'
class MultNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        super().__init__('Mult')
        self.left, self.right = left, right
    def calc(self) -> int:
        return self.left.calc() * self.right.calc()
    def __repr__(self) -> str:
        return f'({self.left} * {self.right})'
class DivNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        super().__init__('Div')
        self.left, self.right = left, right
    def calc(self) -> int:
        return self.left.calc() // self.right.calc()
    def __repr__(self) -> str:
        return f'({self.left} // {self.right})'
class ParenNode(ASTNode):
    def __init__(self, child: ASTNode):
        super().__init__('Paren')
        self.child = child
    def calc(self) -> int:
        return self.child.calc()
    def __repr__(self) -> str:
        return f'({self.child})'
class NumberNode(ASTNode):
    def __init__(self, val: int):
        super().__init__('Number')
        self.val = val
    def calc(self) -> int:
        return self.val
    def __repr__(self) -> str:
        return f'{self.val}'

class Parser:
    def __init__(self, tokens: Iterator[Token]):
        self.tokens = tokens
        self.current_token = None
    def parse(self) -> Optional[ASTNode]:
        try:
            self.advance()
        except:
            return None
        return self.expr()
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except:
            self.current_token = None
    def raise_error(self):
        raise Exception('oopsie')

    def expr(self):
        if self.current_token is None: self.raise_error()
        result = self.term()
        while self.current_token is not None and self.current_token.tp in ['Plus', 'Minus']:
            if self.current_token.tp == 'Plus':
                self.advance()
                result = PlusNode(result, self.term())
            elif self.current_token.tp == 'Minus':
                self.advance()
                result = MinusNode(result, self.term())
        return result

    def term(self):
        if self.current_token is None: self.raise_error()
        result = self.factor()
        while self.current_token is not None and self.current_token.tp in ['Mult', 'Div']:
            if self.current_token.tp == 'Mult':
                self.advance()
                result = MultNode(result, self.factor())
            elif self.current_token.tp == 'Div':
                self.advance()
                result = DivNode(result, self.factor())
        return result

    def factor(self):
        if self.current_token is None: self.raise_error()
        if self.current_token.tp == 'Number' and self.current_token.val is not None:
            result = NumberNode(self.current_token.val)
            self.advance()
            return result
        elif self.current_token.tp == 'Minus':
            self.advance()
            result = self.factor()
            return MinusNode(NumberNode(0), result)
        elif self.current_token.tp == 'LParen':
            self.advance()
            result = self.expr()
            if self.current_token.tp != 'RParen': self.raise_error()
            self.advance()
            return ParenNode(result)
        self.raise_error()

class Solution:
    def calculate(self, s: str) -> int:
        node = Parser(Lexer(s).tokens()).parse()
        return (node and node.calc()) or 0

if __name__ == "__main__":
    tests = [
        ('3-2/1', ['3','Minus','2','Div','1'], '(3 - (2 // 1))', 1),
        ('-(2+1)', ['Minus','LParen','2','Plus','1','RParen'], '(0 - ((2 + 1)))', -3),
        ('-3-2/1', ['Minus','3','Minus','2','Div','1'], '((0 - 3) - (2 // 1))', -5),
    ]
    for s,tokens,ast,calc in tests:
        atokens = list(Lexer(s).tokens())
        assert list(map(str, atokens)) == tokens, f'{atokens} != {tokens}'
        aast = Parser(iter(atokens)).parse()
        assert str(aast) == ast, f'{aast} != {ast}'
        assert aast is not None, 'ast is None'
        acalc = aast.calc()
        assert acalc == calc, f'{acalc} != {calc}'
