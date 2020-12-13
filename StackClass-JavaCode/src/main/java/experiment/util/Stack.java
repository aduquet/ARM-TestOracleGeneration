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
        //items.add( x );
//        System.out.print("\n push Stack: "+ x);
        // return  x;
        //Push_mod_1	replaced return value with null
        //Push_mod-2	replaced return value with 0
        //Push_mod-3	removed item.add(x)
        return 0;
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

        return  items.remove(items.size() - 1);
        // Pop_mod-1	negated conditional
        // Mod2 return items.remove( items.size( ) + 1 );
        // Pop_mod-3	replaced return value with null
        // return null;
    }
    
    /**
     * Returns item from the top of the stack.
     * @return the top item.
     * @throws EmptyStackException if stack is empty.
     */


     // Peek Modification
     public Object peek( )
/**
//Mod1_p
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
 {
        if( isEmpty( ) )
            throw new EmptyStackException( );
        return items.get( items.size( ) + 1 );

        // return null;
        //Peek_mod-1	negated conditional
        //Peek_mod-2	Replaced integer subtraction with addition
        //Peek_mod-3	replaced return value with null

    }

    /**
     * Tests if stack is empty.
     * @return true if the stack is empty; false otherwise.
     */


    public boolean isEmpty( )

    {
        return size( ) == 0;
        //return true;
        //return false;
    }

//    isEmp_mod-1	replaced boolean return with true
//    isEmp_mod-2	negated conditional / size() == 1
 /**
    // isEmpty Modification
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
//    size_mod-1	replaced int return with 0
//    size_mod-2	if size>0 then size+100
//    size_mod-3	 if size>1 then (int) 9.78
    /**
    { //return 0;
        // return items.size( );
    }
     */

    {
        if (items.size()>1)
     {
         double myDouble = 9.78;
         return (int) myDouble;
         //return items.size() + 100;
     }
        else{
            return items.size();
     }}

    public void clear( )
    {
//        System.out.print("\n ________");
        //items.add("asda");
        // items.size();
        items.clear();
//        clear_mod-1	removed call
//        clear_mod-2	replaced call clear() with size()
//        clear_mod-3	replaced call clear() with add(some String)

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
