# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


# This file was generated by libcst.codegen.gen_type_mapping
from typing import Dict as TypingDict, Type, Union

from libcst._maybe_sentinel import MaybeSentinel
from libcst._nodes.base import CSTNode
from libcst._nodes.expression import (
    Annotation,
    Arg,
    Asynchronous,
    Attribute,
    Await,
    BaseDictElement,
    BaseElement,
    BaseExpression,
    BaseFormattedStringContent,
    BaseSlice,
    BinaryOperation,
    BooleanOperation,
    Call,
    Comparison,
    ComparisonTarget,
    CompFor,
    CompIf,
    ConcatenatedString,
    Dict,
    DictComp,
    DictElement,
    Element,
    Ellipsis,
    Float,
    FormattedString,
    FormattedStringExpression,
    FormattedStringText,
    From,
    GeneratorExp,
    IfExp,
    Imaginary,
    Index,
    Integer,
    Lambda,
    LeftCurlyBrace,
    LeftParen,
    LeftSquareBracket,
    List,
    ListComp,
    Name,
    NamedExpr,
    Param,
    Parameters,
    ParamSlash,
    ParamStar,
    RightCurlyBrace,
    RightParen,
    RightSquareBracket,
    Set,
    SetComp,
    SimpleString,
    Slice,
    StarredDictElement,
    StarredElement,
    Subscript,
    SubscriptElement,
    Tuple,
    UnaryOperation,
    Yield,
)
from libcst._nodes.module import Module

from libcst._nodes.op import (
    Add,
    AddAssign,
    And,
    AssignEqual,
    BaseAugOp,
    BaseBinaryOp,
    BaseBooleanOp,
    BaseCompOp,
    BaseUnaryOp,
    BitAnd,
    BitAndAssign,
    BitInvert,
    BitOr,
    BitOrAssign,
    BitXor,
    BitXorAssign,
    Colon,
    Comma,
    Divide,
    DivideAssign,
    Dot,
    Equal,
    FloorDivide,
    FloorDivideAssign,
    GreaterThan,
    GreaterThanEqual,
    ImportStar,
    In,
    Is,
    IsNot,
    LeftShift,
    LeftShiftAssign,
    LessThan,
    LessThanEqual,
    MatrixMultiply,
    MatrixMultiplyAssign,
    Minus,
    Modulo,
    ModuloAssign,
    Multiply,
    MultiplyAssign,
    Not,
    NotEqual,
    NotIn,
    Or,
    Plus,
    Power,
    PowerAssign,
    RightShift,
    RightShiftAssign,
    Semicolon,
    Subtract,
    SubtractAssign,
)
from libcst._nodes.statement import (
    AnnAssign,
    AsName,
    Assert,
    Assign,
    AssignTarget,
    AugAssign,
    BaseSmallStatement,
    BaseStatement,
    BaseSuite,
    Break,
    ClassDef,
    Continue,
    Decorator,
    Del,
    Else,
    ExceptHandler,
    ExceptStarHandler,
    Expr,
    Finally,
    For,
    FunctionDef,
    Global,
    If,
    Import,
    ImportAlias,
    ImportFrom,
    IndentedBlock,
    Match,
    MatchAs,
    MatchCase,
    MatchClass,
    MatchKeywordElement,
    MatchList,
    MatchMapping,
    MatchMappingElement,
    MatchOr,
    MatchOrElement,
    MatchPattern,
    MatchSequence,
    MatchSequenceElement,
    MatchSingleton,
    MatchStar,
    MatchTuple,
    MatchValue,
    NameItem,
    Nonlocal,
    Pass,
    Raise,
    Return,
    SimpleStatementLine,
    SimpleStatementSuite,
    Try,
    TryStar,
    While,
    With,
    WithItem,
)
from libcst._nodes.whitespace import (
    BaseParenthesizableWhitespace,
    Comment,
    EmptyLine,
    Newline,
    ParenthesizedWhitespace,
    SimpleWhitespace,
    TrailingWhitespace,
)
from libcst._removal_sentinel import RemovalSentinel


TYPED_FUNCTION_RETURN_MAPPING: TypingDict[Type[CSTNode], object] = {
    Add: BaseBinaryOp,
    AddAssign: BaseAugOp,
    And: BaseBooleanOp,
    AnnAssign: Union[BaseSmallStatement, RemovalSentinel],
    Annotation: Annotation,
    Arg: Union[Arg, RemovalSentinel],
    AsName: AsName,
    Assert: Union[BaseSmallStatement, RemovalSentinel],
    Assign: Union[BaseSmallStatement, RemovalSentinel],
    AssignEqual: Union[AssignEqual, MaybeSentinel],
    AssignTarget: Union[AssignTarget, RemovalSentinel],
    Asynchronous: Asynchronous,
    Attribute: BaseExpression,
    AugAssign: Union[BaseSmallStatement, RemovalSentinel],
    Await: BaseExpression,
    BinaryOperation: BaseExpression,
    BitAnd: BaseBinaryOp,
    BitAndAssign: BaseAugOp,
    BitInvert: BaseUnaryOp,
    BitOr: Union[BaseBinaryOp, MaybeSentinel],
    BitOrAssign: BaseAugOp,
    BitXor: BaseBinaryOp,
    BitXorAssign: BaseAugOp,
    BooleanOperation: BaseExpression,
    Break: Union[BaseSmallStatement, RemovalSentinel],
    Call: BaseExpression,
    ClassDef: Union[BaseStatement, RemovalSentinel],
    Colon: Union[Colon, MaybeSentinel],
    Comma: Union[Comma, MaybeSentinel],
    Comment: Comment,
    CompFor: CompFor,
    CompIf: CompIf,
    Comparison: BaseExpression,
    ComparisonTarget: Union[ComparisonTarget, RemovalSentinel],
    ConcatenatedString: BaseExpression,
    Continue: Union[BaseSmallStatement, RemovalSentinel],
    Decorator: Union[Decorator, RemovalSentinel],
    Del: Union[BaseSmallStatement, RemovalSentinel],
    Dict: BaseExpression,
    DictComp: BaseExpression,
    DictElement: Union[BaseDictElement, RemovalSentinel],
    Divide: BaseBinaryOp,
    DivideAssign: BaseAugOp,
    Dot: Union[Dot, RemovalSentinel],
    Element: Union[BaseElement, RemovalSentinel],
    Ellipsis: BaseExpression,
    Else: Else,
    EmptyLine: Union[EmptyLine, RemovalSentinel],
    Equal: BaseCompOp,
    ExceptHandler: Union[ExceptHandler, RemovalSentinel],
    ExceptStarHandler: Union[ExceptStarHandler, RemovalSentinel],
    Expr: Union[BaseSmallStatement, RemovalSentinel],
    Finally: Finally,
    Float: BaseExpression,
    FloorDivide: BaseBinaryOp,
    FloorDivideAssign: BaseAugOp,
    For: Union[BaseStatement, RemovalSentinel],
    FormattedString: BaseExpression,
    FormattedStringExpression: Union[BaseFormattedStringContent, RemovalSentinel],
    FormattedStringText: Union[BaseFormattedStringContent, RemovalSentinel],
    From: From,
    FunctionDef: Union[BaseStatement, RemovalSentinel],
    GeneratorExp: BaseExpression,
    Global: Union[BaseSmallStatement, RemovalSentinel],
    GreaterThan: BaseCompOp,
    GreaterThanEqual: BaseCompOp,
    If: Union[BaseStatement, RemovalSentinel],
    IfExp: BaseExpression,
    Imaginary: BaseExpression,
    Import: Union[BaseSmallStatement, RemovalSentinel],
    ImportAlias: Union[ImportAlias, RemovalSentinel],
    ImportFrom: Union[BaseSmallStatement, RemovalSentinel],
    ImportStar: ImportStar,
    In: BaseCompOp,
    IndentedBlock: BaseSuite,
    Index: BaseSlice,
    Integer: BaseExpression,
    Is: BaseCompOp,
    IsNot: BaseCompOp,
    Lambda: BaseExpression,
    LeftCurlyBrace: LeftCurlyBrace,
    LeftParen: Union[LeftParen, MaybeSentinel, RemovalSentinel],
    LeftShift: BaseBinaryOp,
    LeftShiftAssign: BaseAugOp,
    LeftSquareBracket: LeftSquareBracket,
    LessThan: BaseCompOp,
    LessThanEqual: BaseCompOp,
    List: BaseExpression,
    ListComp: BaseExpression,
    Match: Union[BaseStatement, RemovalSentinel],
    MatchAs: MatchPattern,
    MatchCase: MatchCase,
    MatchClass: MatchPattern,
    MatchKeywordElement: Union[MatchKeywordElement, RemovalSentinel],
    MatchList: MatchPattern,
    MatchMapping: MatchPattern,
    MatchMappingElement: Union[MatchMappingElement, RemovalSentinel],
    MatchOr: MatchPattern,
    MatchOrElement: Union[MatchOrElement, RemovalSentinel],
    MatchPattern: MatchPattern,
    MatchSequence: MatchPattern,
    MatchSequenceElement: Union[MatchSequenceElement, RemovalSentinel],
    MatchSingleton: MatchPattern,
    MatchStar: MatchStar,
    MatchTuple: MatchPattern,
    MatchValue: MatchPattern,
    MatrixMultiply: BaseBinaryOp,
    MatrixMultiplyAssign: BaseAugOp,
    Minus: BaseUnaryOp,
    Module: Module,
    Modulo: BaseBinaryOp,
    ModuloAssign: BaseAugOp,
    Multiply: BaseBinaryOp,
    MultiplyAssign: BaseAugOp,
    Name: BaseExpression,
    NameItem: Union[NameItem, RemovalSentinel],
    NamedExpr: BaseExpression,
    Newline: Newline,
    Nonlocal: Union[BaseSmallStatement, RemovalSentinel],
    Not: BaseUnaryOp,
    NotEqual: BaseCompOp,
    NotIn: BaseCompOp,
    Or: BaseBooleanOp,
    Param: Union[Param, MaybeSentinel, RemovalSentinel],
    ParamSlash: Union[ParamSlash, MaybeSentinel],
    ParamStar: Union[ParamStar, MaybeSentinel],
    Parameters: Parameters,
    ParenthesizedWhitespace: Union[BaseParenthesizableWhitespace, MaybeSentinel],
    Pass: Union[BaseSmallStatement, RemovalSentinel],
    Plus: BaseUnaryOp,
    Power: BaseBinaryOp,
    PowerAssign: BaseAugOp,
    Raise: Union[BaseSmallStatement, RemovalSentinel],
    Return: Union[BaseSmallStatement, RemovalSentinel],
    RightCurlyBrace: RightCurlyBrace,
    RightParen: Union[RightParen, MaybeSentinel, RemovalSentinel],
    RightShift: BaseBinaryOp,
    RightShiftAssign: BaseAugOp,
    RightSquareBracket: RightSquareBracket,
    Semicolon: Union[Semicolon, MaybeSentinel],
    Set: BaseExpression,
    SetComp: BaseExpression,
    SimpleStatementLine: Union[BaseStatement, RemovalSentinel],
    SimpleStatementSuite: BaseSuite,
    SimpleString: BaseExpression,
    SimpleWhitespace: Union[BaseParenthesizableWhitespace, MaybeSentinel],
    Slice: BaseSlice,
    StarredDictElement: Union[BaseDictElement, RemovalSentinel],
    StarredElement: Union[BaseElement, RemovalSentinel],
    Subscript: BaseExpression,
    SubscriptElement: Union[SubscriptElement, RemovalSentinel],
    Subtract: BaseBinaryOp,
    SubtractAssign: BaseAugOp,
    TrailingWhitespace: TrailingWhitespace,
    Try: Union[BaseStatement, RemovalSentinel],
    TryStar: Union[BaseStatement, RemovalSentinel],
    Tuple: BaseExpression,
    UnaryOperation: BaseExpression,
    While: Union[BaseStatement, RemovalSentinel],
    With: Union[BaseStatement, RemovalSentinel],
    WithItem: Union[WithItem, RemovalSentinel],
    Yield: BaseExpression,
}
