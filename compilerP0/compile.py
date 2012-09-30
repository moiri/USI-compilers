#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# Simon Maurer
# Lothar Rubusch

"""
USAGE:
$ python ./interp.py ./input.txt

TEST:
$ python ./test_interp.py
"""

import sys
import os.path
import compiler

## abort program
def die( meng ):
    print meng
    sys.exit( -1 )

class Expression( object ):
    def __init( self ):
        # TODO
        pass

## TODO in case: Terminal_Expr and Nonterminal_Expr

class Expr_Stmt( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass


class Expr_Add( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Sub( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass


class Expr_Mul( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass


class Expr_Div( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Const( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Discard( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_AssName( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Assign( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Name( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_CallFunc( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Printnl( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_UnarySub( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_UnaryAdd( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Bitand( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Bitor( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass

class Expr_Bitxor( Expression ):
    def __init( self ):
        # TODO
        pass
    def __str__( self ):
        # TODO
        pass



## P0 compiler implementation
class Engine( object ):
    def __init__( self, filepath=None ):
        if filepath:
            if not os.path.exists( filepath ):
                die( "ERROR: file '%s' does not exist" % filepath )
            else:
                try:
                    ## provided AST
                    self.ast = compiler.parseFile( filepath )
                except SyntaxError:
                    die( "ERROR: invalid syntax in file '%s'" %filepath )

        ## working stack
        self.stack = []

        ## last element, removed from stack
        self.ans = ''

        ## lookup table for symbols
        self.vartable = {'input':'input'}

        self.var_counter = 0

        self.flat_ast = []

    def compile_file( self ):
        try:
            return self.flatten_ast( self.ast )
        except AttributeError:
            ## specific case: TEST mode starts class without providing a P0 code
            ## file, so there won't be an AST already available here
            die( "ERROR: class started in TEST mode, no AST file set" )

    def stack_push( self, elem):
        self.stack.append( elem )

    def stack_pop( self ):
        try:
            val = self.stack.pop()
        except IndexError:
            die( "ERROR: stack index out of bounds" )
        self.ans = str( val )
        return val

    def stack_ans( self ):
        return self.ans

    def vartable_set( self, name, val ):
        self.vartable.update( {name:val} )

    def vartable_get( self, name ):
        try:
            return self.vartable[name]
        except KeyError:
            die( "ERROR: variable '%s' does not exist" % name )

    def check_plain_integer( self, val ):
        if type( val ) is not int:
            die( "ERROR: syntax error, no plain integer allowed" )
        return val

    # TODO  
    def num_child_nodes( self, node ):
        num = sum([self.num_nodes(x) for x in node.getChildNodes()])
        return num

    def gen_varname( self ):
        self.var_counter += 1
        print "new var t%d" %self.var_counter
        return 't' + str(self.var_counter)

    ## function to interprete the ast
    ## @param obj node: node of the ast
    # TODO 
    def num_nodes(self, node):
        return 1 + self.num_child_nodes(node);

    ## function to flatten the ast
    ## @param obj node: node of the ast
    def flatten_ast(self, node):
        if isinstance( node, compiler.ast.Module):
            print "Module"
            return self.flatten_ast(node.node)

        elif isinstance( node, compiler.ast.Stmt):
            print "Stmt"
            for n in node.nodes:
                self.flatten_ast(n) 
            return compiler.ast.Stmt(self.flat_ast)

        elif isinstance(node, compiler.ast.Add):
            print "Add"
            expr = compiler.ast.Add((self.flatten_ast(node.left), self.flatten_ast(node.right)))
            new_varname = self.gen_varname()
            nodes = compiler.ast.AssName(new_varname, 'OP_ASSIGN')
            self.flat_ast.append(compiler.ast.Assign([nodes], expr))
            print "Add: new code line, append Assign", new_varname
            return compiler.ast.Name(new_varname)

        elif isinstance(node, compiler.ast.Mul ):
            print "Mul"
            expr = compiler.ast.Mul(self.flatten_ast(node.left), self.flatten_ast(node.right))
            new_varname = self.gen_varname()
            nodes = compiler.ast.AssName(new_varname, 'OP_ASSIGN')
            self.flat_ast.append(compiler.ast.Assign([nodes], expr))
            print "Mul: new code line, append Assign", new_varname
            return compiler.ast.Name(new_varname)

        elif isinstance(node, compiler.ast.Sub ):
            print "Sub"
            expr = compiler.ast.Sub(self.flatten_ast(node.left), self.flatten_ast(node.right))
            new_varname = self.gen_varname()
            nodes = compiler.ast.AssName(new_varname, 'OP_ASSIGN')
            self.flat_ast.append(compiler.ast.Assign([nodes], expr))
            print "Sub: new code line, append Assign", new_varname
            return compiler.ast.Name(new_varname)

        elif isinstance(node, compiler.ast.Div ):
            print "Div"
            expr = compiler.ast.Div(self.flatten_ast(node.left), self.flatten_ast(node.right))
            new_varname = self.gen_varname()
            nodes = compiler.ast.AssName(new_varname, 'OP_ASSIGN')
            self.flat_ast.append(compiler.ast.Assign([nodes], expr))
            print "Div: new code line, append Assign", new_varname
            return compiler.ast.Name(new_varname)

        elif isinstance(node, compiler.ast.Const):
            print "Const"
            return node

        elif isinstance(node, compiler.ast.Discard):
            print "Discard"
            return

        elif isinstance(node, compiler.ast.AssName ):
            print "AssName"
            return node

        elif isinstance( node, compiler.ast.Assign ):
            print "Assign"
            nodes = self.flatten_ast(node.nodes[0])
            expr = self.flatten_ast(node.expr)
            self.flat_ast.append(compiler.ast.Assign([nodes], expr))
            print "Assign: new code line, append Assign"
            return

        elif isinstance( node, compiler.ast.Name ):
            print "Name"
            return node

        elif isinstance( node, compiler.ast.CallFunc ):
            print "CallFunc"
            expr = compiler.ast.CallFunc(self.flatten_ast(node.node), [])
            new_varname = self.gen_varname()
            nodes = compiler.ast.AssName(new_varname, 'OP_ASSIGN')
            self.flat_ast.append(compiler.ast.Assign([nodes], expr))
            print "CallFunc: new code line, append Assign", new_varname
            return compiler.ast.Name(new_varname)
            
        elif isinstance( node, compiler.ast.Printnl ):
            print "Printnl"
            self.flat_ast.append(compiler.ast.Printnl(self.flatten_ast(node.nodes[0]), None))
            print "Printnl: new code line, append Printnl"
            return

        elif isinstance( node, compiler.ast.UnarySub ):
            print "UnarySub"
            return compiler.ast.UnarySub(self.flatten_ast(node.expr))
 
        elif isinstance( node, compiler.ast.UnaryAdd ):
            print "UnaryAdd"
            return compiler.ast.UnaryAdd(self.flatten_ast(node.expr))

        elif isinstance( node, compiler.ast.Bitand ):
            print "Bitand"
            pass

        elif isinstance( node, compiler.ast.Bitor ):
            print "Bitor"
            pass

        elif isinstance( node, compiler.ast.Bitxor ):
            print "Bitxor"
            pass

        else:
            die( "unknown AST node" )


    ## function to compile a flatten ast 
    ## @param obj node: node of the ast
    def compile(self, node):
        pass

## start
if 1 == len( sys.argv[1:] ):
    compl = Engine( sys.argv[1] )
    compl.compile_file()
    print "AST:", compl.ast
    print "FLAT_AST:", compl.flat_ast