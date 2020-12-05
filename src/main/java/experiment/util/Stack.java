package experiment.util;

import java.io.Serializable;

/**
 * Stack class. Unlike java.util.Stack, this is not
 * extended from Vector. This is the minimum respectable
 * set of operations.
 */
public class Stack implements Serializable
{
    /**
     * Constructs an empty stack.
     */
    public Stack( )
    {
        items = new ArrayList( );
    }
    
    /**
     * Adds an item to the top of the stack.
     * @param x the item to add.
     * @return the item added.
     */
    public Object push( Object x )
    {
        items.add( x );
//        System.out.print("\n push Stack: "+ x);
        return  x;
        // Mod1 push return null;
    }

    public Object pushs( )
    {
        if( isEmpty( ) )
            throw new EmptyStackException( );

        return items.get( items.size( ) - 1 );
    }
    
    /**
     * Removes and returns item from the top of the stack.
     * @return the former top item.
     * @throws EmptyStackException if stack is empty.
     */
    public Object pop( )
    {
//        System.out.print("\n ******");
        if ( isEmpty( ) )
            throw new EmptyStackException( );
            
        return items.remove( items.size( ) - 1 );
        //return null;
    }
    
    /**
     * Returns item from the top of the stack.
     * @return the top item.
     * @throws EmptyStackException if stack is empty.
     */

    /**
     // Peek Modification

     {
     if( isEmpty( ) )
     throw new EmptyStackException( );

     if (items.size() >= 2){
     return items.get( items.size( )-2);
     }
     else{
     return items.get(items.size() - 1);
     }}
     */

    public Object peek( )
    {
        if( isEmpty( ) )
            throw new EmptyStackException( );
        return items.get( items.size( ) - 1 );
        //return null;
    }

    /**
     * Tests if stack is empty.
     * @return true if the stack is empty; false otherwise.
     */


    public boolean isEmpty( )
    {
        return size( ) == 0;
        //return false;
    }

    /**
     * // isEmpty Modification
    {
        if (size( ) == 2){
            return size( ) == 2;
        }
        else {
            return size() == 0;
        }
    }
    */

    /** * Returns the size of the stack.
     * @return the size of the stack.
     */

    // Size Modification

    public int size( )

    {
        return items.size( );
    }
    /**
    {
        if (items.size()>0)
     {
         double myDouble = 9.78;
         return (int) myDouble;
     }
        else{
            return items.size();
     }}
     */

    public void clear( )
    {
//        System.out.print("\n ________");
        // items.add("asda");
        items.clear();
    }

    public String toString( )
    {
        StringBuffer result = new StringBuffer( );
        for( int i = size( ) - 1; i >= 0; i-- )
            result.append(

                // fix: avoid (unbound) recursion if Stack contains itself directly or indirectly
        		(items.get(i) instanceof Stack) ? "Stack["+((Stack)items.get(i)).size()+"]" :
        	    // end of fix

            	items.get( i )
            );
        return result.toString( );
    }

    private ArrayList items;
}
